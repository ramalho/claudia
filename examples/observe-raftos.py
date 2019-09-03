import argparse
import asyncio
import datetime
import logging
import sys
from functools import partial, update_wrapper

import raftos
import structlog
from structlog.stdlib import LoggerFactory
from structlog.processors import JSONRenderer


log = structlog.get_logger()


async def register_raftos(self_id, cluster):
    if not cluster:
        cluster = ["127.0.0.1:8000", "127.0.0.1:8001", "127.0.0.1:8002"]
    myself = cluster[self_id]
    others = cluster[:self_id] + cluster[self_id+1:]
    log.info("Registering Raftos service", self_id=self_id, cluster=cluster)
    await raftos.register(
        # node running on this machine
        myself,

        # other servers
        cluster=others,
    )
    log.info("Completed registration.")


states = {
    raftos.state.Leader: "leader",
    raftos.state.Follower: "follower",
    raftos.state.Candidate: "candidate",
}


def get_state(server):
    return type(server)  # states.get(server.state, None)


def log_state(state_type):
    log.info("Server became", state_type=state_type)
    

def setup_intercepts():
    from raftos.server import Node

    wrapped_send = Node.send
    
    async def intercept_send(self, data, destination):
        log.info("Send", state=get_state(self), destination=destination, data=repr(data))
        await wrapped_send(self, data, destination)

    update_wrapper(intercept_send, wrapped_send)
    Node.send = intercept_send


def get_args():
    parser = argparse.ArgumentParser(description="Observe Raftos implementation")
    parser.add_argument("cluster_id", type=int, help="Cluster ID")
    parser.add_argument("cluster", nargs="*", help="Cluster")
    parser.add_argument("--log-dir", help="Write log file to this directory")
    return parser.parse_args()




# FIXME sort keys to use more preferred output ordering (if possible for JSON) or follow insertion ordering in the actual dict!
# FIXME add the logdir support in args, output a reasonable filename based on cluster_id (or host/port) or maybe don't care
# could do --logfile instead

def setup_logging(args):
    global log
    
    logging.basicConfig(stream=sys.stdout, format="%(message)s")
    def add_timestamp(_, __, event_dict):
        event_dict["timestamp"] = datetime.datetime.utcnow()
        return event_dict
    log = structlog.wrap_logger(
        logging.getLogger(__name__),
        processors=[
            add_timestamp,
            JSONRenderer(indent=1, sort_keys=True),
        ]
    )


async def watch_nodes():
    while True:
        for node in raftos.server.Node.nodes:
            log.info("Watch", node=node, state=node.state.state)
        await asyncio.sleep(1.0)

        
def main():
    args = get_args()
    # setup_logging(args)  # FIXME this should work!!! but it doesn't yet

    setup_intercepts()
    raftos.configure({
        "on_leader": partial(log_state, "leader"),
        "on_follower": partial(log_state, "follower"),
    })
    
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(register_raftos(args.cluster_id, args.cluster))
        loop.create_task(watch_nodes())
        loop.run_forever()
    except KeyboardInterrupt:
        log.info("Service process interrupted")
    finally:
        loop.close()
        log.info("Successful shutdown of Raftos-based service.")


if __name__ == "__main__":
    main()


# Pulp'd: Pulp in a box

This project aims to provide an easier way to deploy multi-container [pulp](http://www.pulpproject.org/). This extends on the great work done by the pulp maintainers working on [Pulp Docker Packaging](https://github.com/pulp/pulp_packaging/tree/master/dockerfiles).

```sh
Usage:
 ./pulpd [options] <command>

Options:
 -c, --config <config>  Config file to source environment from (default: /etc/pulpd.conf)
 -d, --droot <droot>    The docker root directory to use (default: /var/lib/pulpd/data)
 -h, --help             Show this help message

Commands:
 setup      Command to trigger initial setup and spit out boiler-plate config docker dir
 start      Start all containers
 stop       Stop all containers except database and qpid
 restart    Same as executing stop followed by start
 status     Show docker ps for pulp containers
 <cmd>-<cn> Run command (start|stop|status) for container; where cn is the container name
 shutdown   Stop everything
 show       Show pulpd environment
 control    Internal control command for advanced usage
 pull       Pull all imaged (triggers an update for any out dated images)

Container names:
db, qpid, beat, resource_manager, worker<id>, pulpapi, crane

The control command usage:

 control start <container>
 control stop <container>
 control status <container>

 If 'workers' is used all running workers will be affected. For specific worker,
 use 'worker<id>'.

 To affect all containers; use 'all'.
```

## Quickstart

We assume that you already have pulpd in your `PATH`.

```sh
# create a temporary docker data root
# the default is /var/lib/pulpd/data
mkdir -p ~/pulpd/data

# setup
pulpd -d ~/pulpd/data setup

# start
pulpd -d ~/pulpd/data start

# check status
pulpd -d ~/pulpd/data status
```

For a detailed version of what is happening behind the scenes see [Pulp Docker Registry quickstart guide](https://github.com/pulp/pulp_packaging/blob/master/dockerfiles/docker-quickstart.rst).

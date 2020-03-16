#!/bin/bash
lc() {
    nowMs=$(date +%s)
    (
        pids=""
        cpus=${1:-1}
        seconds=${2:-60}
        echo "[$(date)] loading $cpus CPUs for $seconds seconds"
        echo "[$(date)] Expected completion: [$(date --date=@$(expr $nowMs + $seconds))]"
        trap 'for p in $pids; do kill $p; done' 0
        for ((i=0;i<cpus;i++)); do
            sha1sum /dev/zero &
            pids="$pids $!";
        done
        sleep $seconds
    )
    echo "[$(date)] Done"
}

lc $@


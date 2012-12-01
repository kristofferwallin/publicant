#!/usr/bin/env sh
./playgame.py --player_seed 42 --end_wait=0.25 --verbose --log_dir game_logs --turns 1000 --map_file maps/random_walk/random_walk_02p_02.map "$@" "python ../MyBot.py" "python ../MyBot.py" --turntime 500

#!/usr/bin/env sh
# Run from root of repo!

# Exit script if an error occurs.
set -e

GENERATE_LIST="./helper/generate_list.py"
TIME_COMMAND="/usr/bin/time"
TIME_VERSION="$($TIME_COMMAND -V | awk '$0="# "$0')"
TYPES=(random sorted reverse_sorted unique similar)

if [ -z "$1" ]; then
    TIMES=1
else
    TIMES="$1"
fi

if [ -z "$2" ]; then
    LENGTH=100
else
    LENGTH="$2"
fi

CLEAR_LOG=$4

SCRIPT=$5

if [ -z "$3" ]; then
    AMOUNT="$LENGTH"
else
    AMOUNT="$3"
fi

if [ -z "$6" ]; then 
    LOG_FILE="./log/result.csv"
else
    LOG_FILE="$6"
fi


# if [ -z "$4" ]; then
#     COUNT=10
# else
#     COUNT="$4"
# fi

log() {
    DATA=$1
    if [ -z "$DATA" ]; then
        return 1
    fi
    echo "$DATA" >> $LOG_FILE
}

clear_log() {
    echo -n "" > $LOG_FILE
}

init_log() {
    log "Script;List type;Length;Max Int;Input;Time"
}

test() {
    TYPE=$1
    AMOUNT=$2
    OUTPUT=$($GENERATE_LIST $TYPE $LENGTH $AMOUNT)
    LIST=$(awk "NR==1" <<< "$OUTPUT")
    BITS=$(awk "NR==2" <<< "$OUTPUT")
    INPUT="$LIST $BITS"
    # echo "echo $LIST\n$BITS | $TIME_COMMAND -f %e $SCRIPT" 1>&2
    TIME=$(echo -e "$LIST\n$BITS" | $TIME_COMMAND -f %e $SCRIPT 2>&1)
    echo "$SCRIPT;$TYPE;$LENGTH;$AMOUNT;$INPUT;$TIME"
    echo "$TYPE with $SCRIPT took $TIME" "s" 1>&2
}


if [ "$CLEAR_LOG" = true ]; then
    echo "Clearing log"
    clear_log
    init_log
fi

for type in ${TYPES[@]}; do
    for i in $(seq $TIMES); do
        if [ $type = "similar" ]; then
            log "$(test $type $((LENGTH/10-1)))"
        else
            log "$(test $type $AMOUNT)"
        fi
    done
done

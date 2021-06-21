now=$(date +"%Y-%m-%d_%H_%M_%S")

# export PYTHONPATH=$(pwd):$PYTHONPATH

mkdir -p logs
nice -n 5 python workflow/execute.py |& tee logs/${now}_workflow.log

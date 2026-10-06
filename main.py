from summarize import (
    save_checkpoint,
    load_checkpoint
)

state = {
    "current_task": "Buy Milk"
}

save_checkpoint(state)

print("Checkpoint saved")

loaded_state = load_checkpoint()

print(
    "Recovered:",
    loaded_state
)
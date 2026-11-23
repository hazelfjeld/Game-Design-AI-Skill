# Prototype feeding response
var preferred_food = "kelp"
func response(food):
    return "happy" if food == preferred_food else "neutral"
# Engineer work in progress: separate preference and hunger signals.

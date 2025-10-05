from uMotion import uMotion, MODE_RAW

motion = uMotion(camera_index=0, width=160, height=120)
motion.set_mode(MODE_RAW)
motion.set_threshold(10)

try:
    while True:
        motion.update()  # prints "." for changed pixels and " " for unchanged
except KeyboardInterrupt:
    motion.release()
    print("Exiting...")

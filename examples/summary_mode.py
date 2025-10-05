from uMotion import uMotion, MODE_SUMMARY

motion = uMotion(camera_index=0, width=160, height=120)
motion.set_mode(MODE_SUMMARY)
motion.set_threshold(10)

try:
    while True:
        motion.update()
        if motion.motion_detected():
            print(f"[Motion Detected] Pixels: {motion.motion_pixels} | Ratio: {motion.motion_ratio:.4f}")
except KeyboardInterrupt:
    motion.release()
    print("Exiting...")

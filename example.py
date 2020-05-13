# This example play sound from wav-file
import epsound
import time

if __name__ == "__main__":
    # Let's create object of class WavPlayer and add sound from file with name "one" to him
    p = epsound.WavPlayer()
    p.add_sound(file="sound.wav", name="one")
    # Then play our sound 1 sec and print his duration
    p.play("one")
    print(p.sounds["one"].duration)
    time.sleep(1)

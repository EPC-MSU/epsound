# This example play sound from wav-file
import epsound
import time

if __name__ == "__main__":
    # Create object of class WavFile with sound and print his duration
    p_file = epsound.WavFile("sound.wav")
    print("Duration of this sound: {}".format(p_file.duration))
    # Let's create object of class WavPlayer and add sound from file with name "one" to him
    p = epsound.WavPlayer()
    p.add_sound(file="sound.wav", name="one")
    # Then play our sound 1 sec
    p.play("one")
    time.sleep(1)

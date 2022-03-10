# This example plays sound from wav-file
import time
import epsound


if __name__ == "__main__":
    # Let's create object of class WavPlayer and add sound from file with name "one"
    player = epsound.WavPlayer()
    player.add_sound(file_name="sound.wav", sound_name="one")
    # Then play our sound 1 sec and print his duration
    player.play("one")
    print(player.sounds["one"].duration)
    time.sleep(1)

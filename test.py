# Import the random and simpleaudio modules
import random
import simpleaudio
import math
import numpy as np

# Define a function that generates a sine wave with a given frequency and duration
def generate_sine_wave(frequency, duration):
    # Define the sample rate and the number of samples
    sample_rate = 44100
    num_samples = int(duration * sample_rate)
    # Define the amplitude and the angular frequency
    amplitude = 0.5
    angular_frequency = 2 * math.pi * frequency
    # Generate the samples using numpy
    samples = np.sin(np.arange(num_samples) * angular_frequency / sample_rate)
    # Scale and convert the samples to 16-bit integers
    samples = (samples * amplitude * 32767).astype(np.int16)
    # Return the samples as bytes
    return samples.tobytes()

# Define a list of musical notes and their frequencies in Hz
notes = [("C4", 261.63), ("D4", 293.66), ("E4", 329.63), ("F4", 349.23), ("G4", 392.00), ("A4", 440.00), ("B4", 493.88), ("C5", 523.25)]

# Define a function that plays a random note for a given duration
def play_random_note(duration):
    sample_rate = 44100
    # Choose a random note from the list
    note, frequency = random.choice(notes)
    # Print the note name
    print(f"Playing {note}")
    # Generate the sine wave with the given frequency and duration
    wave = generate_sine_wave(frequency, duration)
    # Play the wave using simpleaudio
    simpleaudio.play_buffer(wave, 1, 2, sample_rate).wait_done()

# Define a function that generates a random melody with a given number of notes
def generate_random_melody(num_notes):
    # Loop for the number of notes
    for i in range(num_notes):
        # Choose a random duration between 0.25 and 1 seconds
        duration = random.uniform(0.25, 1)
        # Play a random note with the chosen duration
        play_random_note(duration)

# Generate a random melody with 10 notes
generate_random_melody(10)

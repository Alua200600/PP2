import pygame

pygame.init()
images = ['still_with_you_resized.jpg', 'life_goes_on_resized.jpg', 'black_swan_resized.jpg']
playlist = ['still_with_you.mp3', 'life_goes_on.mp3', 'black_swan.mp3']
current_track = 0

def play_music(track_index):
        pygame.mixer.music.load(playlist[track_index])
        pygame.mixer.music.play()

def set_image(im_index):
        image = pygame.image.load(images[im_index])
        screen.blit(image, (0, 0)) 

screen = pygame.display.set_mode((300, 300))
done = False
paused = True

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                if pygame.mixer.music.get_busy():
                                        pygame.mixer.music.pause()
                                        paused = True
                                else:
                                        pygame.mixer.music.unpause()
                                        paused = False
                        elif event.key == pygame.K_RIGHT:  
                                current_track = (current_track + 1) % len(playlist)
                                set_image(current_track)
                                play_music(current_track)
                                paused = False
                        elif event.key == pygame.K_LEFT:
                                current_track = (current_track - 1) % len(playlist)
                                set_image(current_track)
                                play_music(current_track)
                                paused = False
        
        pygame.display.flip()
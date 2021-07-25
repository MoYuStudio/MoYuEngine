from moviepy.editor import VideoFileClip
import pygame

pygame.display.set_caption('My video!')
pygame.display.set_mode((1280, 720))

clip = VideoFileClip('2021-05-20 23-17-00.mp4')
clip.preview()
pygame.quit()

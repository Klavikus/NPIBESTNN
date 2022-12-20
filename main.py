from video_processing import VideoProcessing

N2V_MODEL_NAME = 'n2v_64x64_05_256_5'
N2V_MODEL_DIR = 'models'
SAMPLE_NAME = 'Mov_S5'

INPUT_PATH = r'./dOut/frames_out/'
OUTPUT_PATH = r'./dOut/frames_out/denoised/'

if __name__ == '__main__':
    vp = VideoProcessing(SAMPLE_NAME, N2V_MODEL_DIR, N2V_MODEL_NAME)
    vp.process()

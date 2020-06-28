import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

inputFilesPath='./inputFiles/'
outputFilesPath='./outputFiles/'


if not os.path.exists(outputFilesPath):
    os.mkdir(outputFilesPath)



def SlipAudioFile(filePath,startId=0):   
    print(f"SlipAudioFile :{filePath}     startId={startId}")
    sound = AudioSegment.from_mp3(filePath)
    loudness = sound.dBFS
    # print(loudness)
    
    chunks = split_on_silence(sound,
        # must be silent for at least half a second,沉默半秒
        min_silence_len=430,
    
        # consider it silent if quieter than -16 dBFS
        silence_thresh=-45,
        keep_silence=400
    
    )
    print('总分段：', len(chunks))
    
    # 放弃长度小于2秒的录音片段
    unUseShort = 500
    unUseLong = 10000
    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) <= unUseShort or len(chunks[i]) >= unUseLong:
            chunks.pop(i)
    print(f'有效分段(大于{unUseShort}ms小于{unUseLong}ms)：', len(chunks))
    
    '''
    for x in range(0,int(len(sound)/1000)):
        print(x,sound[x*1000:(x+1)*1000].max_dBFS)
    '''
    
    for i, chunk in enumerate(chunks):
        fileName = ''

        id = startId + i

        if id < 10:
            fileName = f"000{id}.wav"
        elif id < 100:
            fileName = f"00{id}.wav"
        elif id < 1000:
            fileName = f"0{id}.wav"
        else:
            fileName = f"{id}.wav"
        chunk.export(f"{outputFilesPath}/{fileName}", format="wav")
    
    return len(chunks)

# get all files
files = []
for root, dirs, files in os.walk(inputFilesPath):
    pass

chunkId = 896
for f in files:
    chunkId += SlipAudioFile(inputFilesPath+f,chunkId)


from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class FFmpegSettings(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def format(self):
        '''(Enum) Output file format
        
        [MPEG1, MPEG2, MPEG4, AVI, QUICKTIME, DV, H264, XVID, OGG, MKV, FLASH]'''
        return str()
    @property
    def codec(self):
        '''(Enum) FFmpeg codec to use
        
        [NONE, MPEG1, MPEG2, MPEG4, HUFFYUV, DV, H264, THEORA, FLASH, FFV1,
        QTRLE, DNXHD, PNG]'''
        return str()
    @property
    def video_bitrate(self):
        '''(Integer) Video bitrate (kb/s)'''
        return int()
    @property
    def minrate(self):
        '''(Integer) Rate control: min rate (kb/s)'''
        return int()
    @property
    def maxrate(self):
        '''(Integer) Rate control: max rate (kb/s)'''
        return int()
    @property
    def muxrate(self):
        '''(Integer) Mux rate (bits/s(!))'''
        return int()
    @property
    def gopsize(self):
        '''(Integer) Distance between key frames'''
        return int()
    @property
    def buffersize(self):
        '''(Integer) Rate control: buffer size (kb)'''
        return int()
    @property
    def packetsize(self):
        '''(Integer) Mux packet size (byte)'''
        return int()
    @property
    def use_autosplit(self):
        '''(Boolean) Autosplit output at 2GB boundary'''
        return bool()
    @property
    def use_lossless_output(self):
        '''(Boolean) Use lossless output for video streams'''
        return bool()
    @property
    def audio_codec(self):
        '''(Enum) FFmpeg audio codec to use
        
        [NONE, MP2, MP3, AC3, AAC, VORBIS, FLAC, PCM]'''
        return str()
    @property
    def audio_bitrate(self):
        '''(Integer) Audio bitrate (kb/s)'''
        return int()
    @property
    def audio_volume(self):
        '''(Float) Audio volume'''
        return float()
    @property
    def audio_mixrate(self):
        '''(Integer) Audio samplerate(samples/s)'''
        return int()
    @property
    def audio_channels(self):
        '''(Enum) Audio channel count
        
        [MONO, STEREO, SURROUND4, SURROUND51, SURROUND71]'''
        return str()
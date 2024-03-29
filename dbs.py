command_lengths_x = [
    0,  # END
    1,  # TIME
    4,  # MIKU_MOVE
    2,  # MIKU_ROT
    2,  # MIKU_DISP
    2,  # MIKU_SHADOW
    12,  # TARGET
    4,  # SET_MOTION
    2,  # SET_PLAYDATA
    6,  # EFFECT
    2,  # FADEIN_FIELD
    1,  # EFFECT_OFF
    6,  # SET_CAMERA
    2,  # DATA_CAMERA
    2,  # CHANGE_FIELD
    1,  # HIDE_FIELD
    3,  # MOVE_FIELD
    2,  # FADEOUT_FIELD
    3,  # EYE_ANIM
    5,  # MOUTH_ANIM
    5,  # HAND_ANIM
    4,  # LOOK_ANIM
    4,  # EXPRESSION
    5,  # LOOK_CAMERA
    2,  # LYRIC
    0,  # MUSIC_PLAY
    2,  # MODE_SELECT
    4,  # EDIT_MOTION
    2,  # BAR_TIME_SET
    2,  # SHADOWHEIGHT
    1,  # EDIT_FACE
    21,  # MOVE_CAMERA
    0,  # PV_END
    3,  # SHADOWPOS
    2,  # EDIT_LYRIC
    5,  # EDIT_TARGET
    1,  # EDIT_MOUTH
    1,  # SET_CHARA
    7,  # EDIT_MOVE
    1,  # EDIT_SHADOW
    1,  # EDIT_EYELID
    2,  # EDIT_EYE
    1,  # EDIT_ITEM
    2,  # EDIT_EFFECT
    1,  # EDIT_DISP
    2,  # EDIT_HAND_ANIM
    3,  # AIM
    3,  # HAND_ITEM
    1,  # EDIT_BLUSH
    2,  # NEAR_CLIP
    2,  # CLOTH_WET
    3,  # LIGHT_ROT
    6,  # SCENE_FADE
    6,  # TONE_TRANS
    1,  # SATURATE
    1,  # FADE_MODE
    2,  # AUTO_BLINK
    3,  # PARTS_DISP
    1,  # TARGET_FLYING_TIME
    2,  # CHARA_SIZE
    2,  # CHARA_HEIGHT_ADJUST
    4,  # ITEM_ANIM
    4,  # CHARA_POS_ADJUST
    1,  # SCENE_ROT
    2,  # EDIT_MOT_SMOOTH_LEN
    1,  # PV_BRANCH_MODE
    2,  # DATA_CAMERA_START
    1,  # MOVIE_PLAY
    1,  # MOVIE_DISP
    3,  # WIND
    3,  # OSAGE_STEP
    3,  # OSAGE_MV_CCL
    2,  # CHARA_COLOR
    1,  # SE_EFFECT
    9,  # EDIT_MOVE_XYZ
    3,  # EDIT_EYELID_ANIM
    2,  # EDIT_INSTRUMENT_ITEM
    4,  # EDIT_MOTION_LOOP
    2,  # EDIT_EXPRESSION
    3,  # EDIT_EYE_ANIM
    2,  # EDIT_MOUTH_ANIM
    22,  # EDIT_CAMERA
    1,  # EDIT_MODE_SELECT
    2,  # PV_END_FADEOUT
    1,  # CREDIT_TITLE
    1,  # BAR_POINT
    1,  # BEAT_POINT
    9,  # RESERVE
    2,  # PV_AUTH_LIGHT_PRIORITY
    3,  # PV_CHARA_LIGHT
    3,  # PV_STAGE_LIGHT
    11,  # TARGET_EFFECT
    3,  # FOG
    2,  # BLOOM
    3,  # COLOR_CORRECTION
    3,  # DOF
    4,  # CHARA_ALPHA
    1,  # AUTO_CAPTURE_BEGIN
    1,  # MANUAL_CAPTURE
    3,  # TOON_EDGE
    3,  # SHIMMER
    4,  # ITEM_ALPHA
    1,  # MOVIE_CUT
    112,  # EDIT_CAMERA_BOX
    1,  # EDIT_STAGE_PARAM
    1,  # EDIT_CHANGE_FIELD
    7,  # MIKUDAYO_ADJUST
    2,  # LYRIC_2
    2,  # LYRIC_READ
    2,  # LYRIC_READ_2
    5,  # ANNOTATION
    2,  # STAGE_EFFECT
    3,  # SONG_EFFECT
    3,  # SONG_EFFECT_ATTACH
    2,  # LIGHT_AUTH
    2,  # FADE
    2,  # SET_STAGE_EFFECT_ENV
    2,  # COMMON_EFFECT_AET_FRONT
    2,  # COMMON_EFFECT_AET_FRONT_LOW
    2,  # COMMON_EFFECT_PARTICLE
    3,  # SONG_EFFECT_ALPHA_SORT
    5,  # LOOK_CAMERA_FACE_LIMIT
    3,  # ITEM_LIGHT
    3,  # CHARA_EFFECT
    2,  # MARKER
    3,  # CHARA_EFFECT_CHARA_LIGHT
    2,  # ENABLE_COMMON_LIGHT_TO_CHARA
    2,  # ENABLE_FXAA
    2,  # ENABLE_TEMPORAL_AA
    2,  # ENABLE_REFLECTION
    2,  # BANK_BRANCH
    2,  # BANK_END
    2,  # VR_LIVE_MOVIE
    2,  # VR_CHEER
    2,  # VR_CHARA_PSMOVE
    2,  # VR_MOVE_PATH
    2,  # VR_SET_BASE
    2,  # VR_TECH_DEMO_EFFECT
    2,  # VR_TRANSFORM
    2,  # GAZE
    2,  # TECH_DEMO_GESUTRE
    2,  # VR_CHEMICAL_LIGHT_COLOR
    5,  # VR_LIVE_MOB
    9,  # VR_LIVE_HAIR_OSAGE
    9,  # VR_LIVE_LOOK_CAMERA
    5,  # VR_LIVE_CHEER
    3,  # VR_LIVE_GESTURE
    7,  # VR_LIVE_CLONE
    7,  # VR_LOOP_EFFECT
    6,  # VR_LIVE_ONESHOT_EFFECT
    9,  # VR_LIVE_PRESENT
    5,  # VR_LIVE_TRANSFORM
    5,  # VR_LIVE_FLY
    2,  # VR_LIVE_CHARA_VOICE
]

command_lengths_f = [
    0,  # END
    1,  # TIME
    4,  # MIKU_MOVE
    2,  # MIKU_ROT
    2,  # MIKU_DISP
    2,  # MIKU_SHADOW
    11,  # TARGET
    4,  # SET_MOTION
    2,  # SET_PLAYDATA
    6,  # EFFECT
    2,  # FADEIN_FIELD
    1,  # EFFECT_OFF
    6,  # SET_CAMERA
    2,  # DATA_CAMERA
    1,  # CHANGE_FIELD
    1,  # HIDE_FIELD
    3,  # MOVE_FIELD
    2,  # FADEOUT_FIELD
    3,  # EYE_ANIM
    5,  # MOUTH_ANIM
    5,  # HAND_ANIM
    4,  # LOOK_ANIM
    4,  # EXPRESSION
    5,  # LOOK_CAMERA
    2,  # LYRIC
    0,  # MUSIC_PLAY
    2,  # MODE_SELECT
    4,  # EDIT_MOTION
    2,  # BAR_TIME_SET
    2,  # SHADOWHEIGHT
    1,  # EDIT_FACE
    21,  # MOVE_CAMERA
    0,  # PV_END
    3,  # SHADOWPOS
    2,  # EDIT_LYRIC
    5,  # EDIT_TARGET
    1,  # EDIT_MOUTH
    1,  # SET_CHARA
    7,  # EDIT_MOVE
    1,  # EDIT_SHADOW
    1,  # EDIT_EYELID
    2,  # EDIT_EYE
    1,  # EDIT_ITEM
    2,  # EDIT_EFFECT
    1,  # EDIT_DISP
    2,  # EDIT_HAND_ANIM
    3,  # AIM
    3,  # HAND_ITEM
    1,  # EDIT_BLUSH
    2,  # NEAR_CLIP
    2,  # CLOTH_WET
    3,  # LIGHT_ROT
    6,  # SCENE_FADE
    6,  # TONE_TRANS
    1,  # SATURATE
    1,  # FADE_MODE
    2,  # AUTO_BLINK
    3,  # PARTS_DISP
    1,  # TARGET_FLYING_TIME
    2,  # CHARA_SIZE
    2,  # CHARA_HEIGHT_ADJUST
    4,  # ITEM_ANIM
    4,  # CHARA_POS_ADJUST
    1,  # SCENE_ROT
    2,  # MOT_SMOOTH
    1,  # PV_BRANCH_MODE
    2,  # DATA_CAMERA_START
    1,  # MOVIE_PLAY
    1,  # MOVIE_DISP
    3,  # WIND
    3,  # OSAGE_STEP
    3,  # OSAGE_MV_CCL
    2,  # CHARA_COLOR
    1,  # SE_EFFECT
    9,  # EDIT_MOVE_XYZ
    3,  # EDIT_EYELID_ANIM
    2,  # EDIT_INSTRUMENT_ITEM
    4,  # EDIT_MOTION_LOOP
    2,  # EDIT_EXPRESSION
    3,  # EDIT_EYE_ANIM
    2,  # EDIT_MOUTH_ANIM
    24,  # EDIT_CAMERA
    1,  # EDIT_MODE_SELECT
    2,  # PV_END_FADEOUT
    2,  # PV_END_FADEOUT
]

command_to_string_x = {
    0x00: 'END',
    0x01: 'TIME',
    0x02: 'MIKU_MOVE',
    0x03: 'MIKU_ROT',
    0x04: 'MIKU_DISP',
    0x05: 'MIKU_SHADOW',
    0x06: 'TARGET',
    0x07: 'SET_MOTION',
    0x08: 'SET_PLAYDATA',
    0x09: 'EFFECT',
    0x0A: 'FADEIN_FIELD',
    0x0B: 'EFFECT_OFF',
    0x0C: 'SET_CAMERA',
    0x0D: 'DATA_CAMERA',
    0x0E: 'CHANGE_FIELD',
    0x0F: 'HIDE_FIELD',
    0x10: 'MOVE_FIELD',
    0x11: 'FADEOUT_FIELD',
    0x12: 'EYE_ANIM',
    0x13: 'MOUTH_ANIM',
    0x14: 'HAND_ANIM',
    0x15: 'LOOK_ANIM',
    0x16: 'EXPRESSION',
    0x17: 'LOOK_CAMERA',
    0x18: 'LYRIC',
    0x19: 'MUSIC_PLAY',
    0x1A: 'MODE_SELECT',
    0x1B: 'EDIT_MOTION',
    0x1C: 'BAR_TIME_SET',
    0x1D: 'SHADOWHEIGHT',
    0x1E: 'EDIT_FACE',
    0x1F: 'MOVE_CAMERA',
    0x20: 'PV_END',
    0x21: 'SHADOWPOS',
    0x22: 'EDIT_LYRIC',
    0x23: 'EDIT_TARGET',
    0x24: 'EDIT_MOUTH',
    0x25: 'SET_CHARA',
    0x26: 'EDIT_MOVE',
    0x27: 'EDIT_SHADOW',
    0x28: 'EDIT_EYELID',
    0x29: 'EDIT_EYE',
    0x2A: 'EDIT_ITEM',
    0x2B: 'EDIT_EFFECT',
    0x2C: 'EDIT_DISP',
    0x2D: 'EDIT_HAND_ANIM',
    0x2E: 'AIM',
    0x2F: 'HAND_ITEM',
    0x30: 'EDIT_BLUSH',
    0x31: 'NEAR_CLIP',
    0x32: 'CLOTH_WET',
    0x33: 'LIGHT_ROT',
    0x34: 'SCENE_FADE',
    0x35: 'TONE_TRANS',
    0x36: 'SATURATE',
    0x37: 'FADE_MODE',
    0x38: 'AUTO_BLINK',
    0x39: 'PARTS_DISP',
    0x3A: 'TARGET_FLYING_TIME',
    0x3B: 'CHARA_SIZE',
    0x3C: 'CHARA_HEIGHT_ADJUST',
    0x3D: 'ITEM_ANIM',
    0x3E: 'CHARA_POS_ADJUST',
    0x3F: 'SCENE_ROT',
    0x40: 'EDIT_MOT_SMOOTH_LEN',
    0x41: 'PV_BRANCH_MODE',
    0x42: 'DATA_CAMERA_START',
    0x43: 'MOVIE_PLAY',
    0x44: 'MOVIE_DISP',
    0x45: 'WIND',
    0x46: 'OSAGE_STEP',
    0x47: 'OSAGE_MV_CCL',
    0x48: 'CHARA_COLOR',
    0x49: 'SE_EFFECT',
    0x4A: 'EDIT_MOVE_XYZ',
    0x4B: 'EDIT_EYELID_ANIM',
    0x4C: 'EDIT_INSTRUMENT_ITEM',
    0x4D: 'EDIT_MOTION_LOOP',
    0x4E: 'EDIT_EXPRESSION',
    0x4F: 'EDIT_EYE_ANIM',
    0x50: 'EDIT_MOUTH_ANIM',
    0x51: 'EDIT_CAMERA',
    0x52: 'EDIT_MODE_SELECT',
    0x53: 'PV_END_FADEOUT',
    0x54: 'CREDIT_TITLE',
    0x55: 'BAR_POINT',
    0x56: 'BEAT_POINT',
    0x57: 'RESERVE',
    0x58: 'PV_AUTH_LIGHT_PRIORITY',
    0x59: 'PV_CHARA_LIGHT',
    0x5A: 'PV_STAGE_LIGHT',
    0x5B: 'TARGET_EFFECT',
    0x5C: 'FOG',
    0x5D: 'BLOOM',
    0x5E: 'COLOR_CORRECTION',
    0x5F: 'DOF',
    0x60: 'CHARA_ALPHA',
    0x61: 'AUTO_CAPTURE_BEGIN',
    0x62: 'MANUAL_CAPTURE',
    0x63: 'TOON_EDGE',
    0x64: 'SHIMMER',
    0x65: 'ITEM_ALPHA',
    0x66: 'MOVIE_CUT',
    0x67: 'EDIT_CAMERA_BOX',
    0x68: 'EDIT_STAGE_PARAM',
    0x69: 'EDIT_CHANGE_FIELD',
    0x6A: 'MIKUDAYO_ADJUST',
    0x6B: 'LYRIC_2',
    0x6C: 'LYRIC_READ',
    0x6D: 'LYRIC_READ_2',
    0x6E: 'ANNOTATION',
    0x6F: 'STAGE_EFFECT',
    0x70: 'SONG_EFFECT',
    0x71: 'SONG_EFFECT_ATTACH',
    0x72: 'LIGHT_AUTH',
    0x73: 'FADE',
    0x74: 'SET_STAGE_EFFECT_ENV',
    0x75: 'COMMON_EFFECT_AET_FRONT',
    0x76: 'COMMON_EFFECT_AET_FRONT_LOW',
    0x77: 'COMMON_EFFECT_PARTICLE',
    0x78: 'SONG_EFFECT_ALPHA_SORT',
    0x79: 'LOOK_CAMERA_FACE_LIMIT',
    0x7A: 'ITEM_LIGHT',
    0x7B: 'CHARA_EFFECT',
    0x7C: 'MARKER',
    0x7D: 'CHARA_EFFECT_CHARA_LIGHT',
    0x7E: 'ENABLE_COMMON_LIGHT_TO_CHARA',
    0x7F: 'ENABLE_FXAA',
    0x80: 'ENABLE_TEMPORAL_AA',
    0x81: 'ENABLE_REFLECTION',
    0x82: 'BANK_BRANCH',
    0x83: 'BANK_END',
    0x84: 'VR_LIVE_MOVIE',
    0x85: 'VR_CHEER',
    0x86: 'VR_CHARA_PSMOVE',
    0x87: 'VR_MOVE_PATH',
    0x88: 'VR_SET_BASE',
    0x89: 'VR_TECH_DEMO_EFFECT',
    0x8A: 'VR_TRANSFORM',
    0x8B: 'GAZE',
    0x8C: 'TECH_DEMO_GESUTRE',
    0x8D: 'VR_CHEMICAL_LIGHT_COLOR',
    0x8E: 'VR_LIVE_MOB',
    0x8F: 'VR_LIVE_HAIR_OSAGE',
    0x90: 'VR_LIVE_LOOK_CAMERA',
    0x91: 'VR_LIVE_CHEER',
    0x92: 'VR_LIVE_GESTURE',
    0x93: 'VR_LIVE_CLONE',
    0x94: 'VR_LOOP_EFFECT',
    0x95: 'VR_LIVE_ONESHOT_EFFECT',
    0x96: 'VR_LIVE_PRESENT',
    0x97: 'VR_LIVE_TRANSFORM',
    0x98: 'VR_LIVE_FLY',
    0x99: 'VR_LIVE_CHARA_VOICE',
}

command_to_string_f = {
    0x00: 'END',
    0x01: 'TIME',
    0x02: 'MIKU_MOVE',
    0x03: 'MIKU_ROT',
    0x04: 'MIKU_DISP',
    0x05: 'MIKU_SHADOW',
    0x06: 'TARGET',
    0x07: 'SET_MOTION',
    0x08: 'SET_PLAYDATA',
    0x09: 'EFFECT',
    0x0A: 'FADEIN_FIELD',
    0x0B: 'EFFECT_OFF',
    0x0C: 'SET_CAMERA',
    0x0D: 'DATA_CAMERA',
    0x0E: 'CHANGE_FIELD',
    0x0F: 'HIDE_FIELD',
    0x10: 'MOVE_FIELD',
    0x11: 'FADEOUT_FIELD',
    0x12: 'EYE_ANIM',
    0x13: 'MOUTH_ANIM',
    0x14: 'HAND_ANIM',
    0x15: 'LOOK_ANIM',
    0x16: 'EXPRESSION',
    0x17: 'LOOK_CAMERA',
    0x18: 'LYRIC',
    0x19: 'MUSIC_PLAY',
    0x1A: 'MODE_SELECT',
    0x1B: 'EDIT_MOTION',
    0x1C: 'BAR_TIME_SET',
    0x1D: 'SHADOWHEIGHT',
    0x1E: 'EDIT_FACE',
    0x1F: 'MOVE_CAMERA',
    0x20: 'PV_END',
    0x21: 'SHADOWPOS',
    0x22: 'EDIT_LYRIC',
    0x23: 'EDIT_TARGET',
    0x24: 'EDIT_MOUTH',
    0x25: 'SET_CHARA',
    0x26: 'EDIT_MOVE',
    0x27: 'EDIT_SHADOW',
    0x28: 'EDIT_EYELID',
    0x29: 'EDIT_EYE',
    0x2A: 'EDIT_ITEM',
    0x2B: 'EDIT_EFFECT',
    0x2C: 'EDIT_DISP',
    0x2D: 'EDIT_HAND_ANIM',
    0x2E: 'AIM',
    0x2F: 'HAND_ITEM',
    0x30: 'EDIT_BLUSH',
    0x31: 'NEAR_CLIP',
    0x32: 'CLOTH_WET',
    0x33: 'LIGHT_ROT',
    0x34: 'SCENE_FADE',
    0x35: 'TONE_TRANS',
    0x36: 'SATURATE',
    0x37: 'FADE_MODE',
    0x38: 'AUTO_BLINK',
    0x39: 'PARTS_DISP',
    0x3A: 'TARGET_FLYING_TIME',
    0x3B: 'CHARA_SIZE',
    0x3C: 'CHARA_HEIGHT_ADJUST',
    0x3D: 'ITEM_ANIM',
    0x3E: 'CHARA_POS_ADJUST',
    0x3F: 'SCENE_ROT',
    0x40: 'MOT_SMOOTH',
    0x41: 'PV_BRANCH_MODE',
    0x42: 'DATA_CAMERA_START',
    0x43: 'MOVIE_PLAY',
    0x44: 'MOVIE_DISP',
    0x45: 'WIND',
    0x46: 'OSAGE_STEP',
    0x47: 'OSAGE_MV_CCL',
    0x48: 'CHARA_COLOR',
    0x49: 'SE_EFFECT',
    0x4A: 'EDIT_MOVE_XYZ',
    0x4B: 'EDIT_EYELID_ANIM',
    0x4C: 'EDIT_INSTRUMENT_ITEM',
    0x4D: 'EDIT_MOTION_LOOP',
    0x4E: 'EDIT_EXPRESSION',
    0x4F: 'EDIT_EYE_ANIM',
    0x50: 'EDIT_MOUTH_ANIM',
    0x51: 'EDIT_CAMERA',
    0x52: 'EDIT_MODE_SELECT',
    0x53: 'PV_END_FADEOUT',
}

string_to_command_x = {
    'END': 0x00,
    'TIME': 0x01,
    'MIKU_MOVE': 0x02,
    'MIKU_ROT': 0x03,
    'MIKU_DISP': 0x04,
    'MIKU_SHADOW': 0x05,
    'TARGET': 0x06,
    'SET_MOTION': 0x07,
    'SET_PLAYDATA': 0x08,
    'EFFECT': 0x09,
    'FADEIN_FIELD': 0x0A,
    'EFFECT_OFF': 0x0B,
    'SET_CAMERA': 0x0C,
    'DATA_CAMERA': 0x0D,
    'CHANGE_FIELD': 0x0E,
    'HIDE_FIELD': 0x0F,
    'MOVE_FIELD': 0x10,
    'FADEOUT_FIELD': 0x11,
    'EYE_ANIM': 0x12,
    'MOUTH_ANIM': 0x13,
    'HAND_ANIM': 0x14,
    'LOOK_ANIM': 0x15,
    'EXPRESSION': 0x16,
    'LOOK_CAMERA': 0x17,
    'LYRIC': 0x18,
    'MUSIC_PLAY': 0x19,
    'MODE_SELECT': 0x1A,
    'EDIT_MOTION': 0x1B,
    'BAR_TIME_SET': 0x1C,
    'SHADOWHEIGHT': 0x1D,
    'EDIT_FACE': 0x1E,
    'MOVE_CAMERA': 0x1F,
    'PV_END': 0x20,
    'SHADOWPOS': 0x21,
    'EDIT_LYRIC': 0x22,
    'EDIT_TARGET': 0x23,
    'EDIT_MOUTH': 0x24,
    'SET_CHARA': 0x25,
    'EDIT_MOVE': 0x26,
    'EDIT_SHADOW': 0x27,
    'EDIT_EYELID': 0x28,
    'EDIT_EYE': 0x29,
    'EDIT_ITEM': 0x2A,
    'EDIT_EFFECT': 0x2B,
    'EDIT_DISP': 0x2C,
    'EDIT_HAND_ANIM': 0x2D,
    'AIM': 0x2E,
    'HAND_ITEM': 0x2F,
    'EDIT_BLUSH': 0x30,
    'NEAR_CLIP': 0x31,
    'CLOTH_WET': 0x32,
    'LIGHT_ROT': 0x33,
    'SCENE_FADE': 0x34,
    'TONE_TRANS': 0x35,
    'SATURATE': 0x36,
    'FADE_MODE': 0x37,
    'AUTO_BLINK': 0x38,
    'PARTS_DISP': 0x39,
    'TARGET_FLYING_TIME': 0x3A,
    'CHARA_SIZE': 0x3B,
    'CHARA_HEIGHT_ADJUST': 0x3C,
    'ITEM_ANIM': 0x3D,
    'CHARA_POS_ADJUST': 0x3E,
    'SCENE_ROT': 0x3F,
    'EDIT_MOT_SMOOTH_LEN': 0x40,
    'PV_BRANCH_MODE': 0x41,
    'DATA_CAMERA_START': 0x42,
    'MOVIE_PLAY': 0x43,
    'MOVIE_DISP': 0x44,
    'WIND': 0x45,
    'OSAGE_STEP': 0x46,
    'OSAGE_MV_CCL': 0x47,
    'CHARA_COLOR': 0x48,
    'SE_EFFECT': 0x49,
    'EDIT_MOVE_XYZ': 0x4A,
    'EDIT_EYELID_ANIM': 0x4B,
    'EDIT_INSTRUMENT_ITEM': 0x4C,
    'EDIT_MOTION_LOOP': 0x4D,
    'EDIT_EXPRESSION': 0x4E,
    'EDIT_EYE_ANIM': 0x4F,
    'EDIT_MOUTH_ANIM': 0x50,
    'EDIT_CAMERA': 0x51,
    'EDIT_MODE_SELECT': 0x52,
    'PV_END_FADEOUT': 0x53,
    'CREDIT_TITLE': 0x54,
    'BAR_POINT': 0x55,
    'BEAT_POINT': 0x56,
    'RESERVE': 0x57,
    'PV_AUTH_LIGHT_PRIORITY': 0x58,
    'PV_CHARA_LIGHT': 0x59,
    'PV_STAGE_LIGHT': 0x5A,
    'TARGET_EFFECT': 0x5B,
    'FOG': 0x5C,
    'BLOOM': 0x5D,
    'COLOR_CORRECTION': 0x5E,
    'DOF': 0x5F,
    'CHARA_ALPHA': 0x60,
    'AUTO_CAPTURE_BEGIN': 0x61,
    'MANUAL_CAPTURE': 0x62,
    'TOON_EDGE': 0x63,
    'SHIMMER': 0x64,
    'ITEM_ALPHA': 0x65,
    'MOVIE_CUT': 0x66,
    'EDIT_CAMERA_BOX': 0x67,
    'EDIT_STAGE_PARAM': 0x68,
    'EDIT_CHANGE_FIELD': 0x69,
    'MIKUDAYO_ADJUST': 0x6A,
    'LYRIC_2': 0x6B,
    'LYRIC_READ': 0x6C,
    'LYRIC_READ_2': 0x6D,
    'ANNOTATION': 0x6E,
    'STAGE_EFFECT': 0x6F,
    'SONG_EFFECT': 0x70,
    'SONG_EFFECT_ATTACH': 0x71,
    'LIGHT_AUTH': 0x72,
    'FADE': 0x73,
    'SET_STAGE_EFFECT_ENV': 0x74,
    'COMMON_EFFECT_AET_FRONT': 0x75,
    'COMMON_EFFECT_AET_FRONT_LOW': 0x76,
    'COMMON_EFFECT_PARTICLE': 0x77,
    'SONG_EFFECT_ALPHA_SORT': 0x78,
    'LOOK_CAMERA_FACE_LIMIT': 0x79,
    'ITEM_LIGHT': 0x7A,
    'CHARA_EFFECT': 0x7B,
    'MARKER': 0x7C,
    'CHARA_EFFECT_CHARA_LIGHT': 0x7D,
    'ENABLE_COMMON_LIGHT_TO_CHARA': 0x7E,
    'ENABLE_FXAA': 0x7F,
    'ENABLE_TEMPORAL_AA': 0x80,
    'ENABLE_REFLECTION': 0x81,
    'BANK_BRANCH': 0x82,
    'BANK_END': 0x83,
    'VR_LIVE_MOVIE': 0x84,
    'VR_CHEER': 0x85,
    'VR_CHARA_PSMOVE': 0x86,
    'VR_MOVE_PATH': 0x87,
    'VR_SET_BASE': 0x88,
    'VR_TECH_DEMO_EFFECT': 0x89,
    'VR_TRANSFORM': 0x8A,
    'GAZE': 0x8B,
    'TECH_DEMO_GESUTRE': 0x8C,
    'VR_CHEMICAL_LIGHT_COLOR': 0x8D,
    'VR_LIVE_MOB': 0x8E,
    'VR_LIVE_HAIR_OSAGE': 0x8F,
    'VR_LIVE_LOOK_CAMERA': 0x90,
    'VR_LIVE_CHEER': 0x91,
    'VR_LIVE_GESTURE': 0x92,
    'VR_LIVE_CLONE': 0x93,
    'VR_LOOP_EFFECT': 0x94,
    'VR_LIVE_ONESHOT_EFFECT': 0x95,
    'VR_LIVE_PRESENT': 0x96,
    'VR_LIVE_TRANSFORM': 0x97,
    'VR_LIVE_FLY': 0x98,
    'VR_LIVE_CHARA_VOICE': 0x99,
}

string_to_command_f = {
    'END': 0x00,
    'TIME': 0x01,
    'MIKU_MOVE': 0x02,
    'MIKU_ROT': 0x03,
    'MIKU_DISP': 0x04,
    'MIKU_SHADOW': 0x05,
    'TARGET': 0x06,
    'SET_MOTION': 0x07,
    'SET_PLAYDATA': 0x08,
    'EFFECT': 0x09,
    'FADEIN_FIELD': 0x0A,
    'EFFECT_OFF': 0x0B,
    'SET_CAMERA': 0x0C,
    'DATA_CAMERA': 0x0D,
    'CHANGE_FIELD': 0x0E,
    'HIDE_FIELD': 0x0F,
    'MOVE_FIELD': 0x10,
    'FADEOUT_FIELD': 0x11,
    'EYE_ANIM': 0x12,
    'MOUTH_ANIM': 0x13,
    'HAND_ANIM': 0x14,
    'LOOK_ANIM': 0x15,
    'EXPRESSION': 0x16,
    'LOOK_CAMERA': 0x17,
    'LYRIC': 0x18,
    'MUSIC_PLAY': 0x19,
    'MODE_SELECT': 0x1A,
    'EDIT_MOTION': 0x1B,
    'BAR_TIME_SET': 0x1C,
    'SHADOWHEIGHT': 0x1D,
    'EDIT_FACE': 0x1E,
    'MOVE_CAMERA': 0x1F,
    'PV_END': 0x20,
    'SHADOWPOS': 0x21,
    'EDIT_LYRIC': 0x22,
    'EDIT_TARGET': 0x23,
    'EDIT_MOUTH': 0x24,
    'SET_CHARA': 0x25,
    'EDIT_MOVE': 0x26,
    'EDIT_SHADOW': 0x27,
    'EDIT_EYELID': 0x28,
    'EDIT_EYE': 0x29,
    'EDIT_ITEM': 0x2A,
    'EDIT_EFFECT': 0x2B,
    'EDIT_DISP': 0x2C,
    'EDIT_HAND_ANIM': 0x2D,
    'AIM': 0x2E,
    'HAND_ITEM': 0x2F,
    'EDIT_BLUSH': 0x30,
    'NEAR_CLIP': 0x31,
    'CLOTH_WET': 0x32,
    'LIGHT_ROT': 0x33,
    'SCENE_FADE': 0x34,
    'TONE_TRANS': 0x35,
    'SATURATE': 0x36,
    'FADE_MODE': 0x37,
    'AUTO_BLINK': 0x38,
    'PARTS_DISP': 0x39,
    'TARGET_FLYING_TIME': 0x3A,
    'CHARA_SIZE': 0x3B,
    'CHARA_HEIGHT_ADJUST': 0x3C,
    'ITEM_ANIM': 0x3D,
    'CHARA_POS_ADJUST': 0x3E,
    'SCENE_ROT': 0x3F,
    'MOT_SMOOTH': 0x40,
    'PV_BRANCH_MODE': 0x41,
    'DATA_CAMERA_START': 0x42,
    'MOVIE_PLAY': 0x43,
    'MOVIE_DISP': 0x44,
    'WIND': 0x45,
    'OSAGE_STEP': 0x46,
    'OSAGE_MV_CCL': 0x47,
    'CHARA_COLOR': 0x48,
    'SE_EFFECT': 0x49,
    'EDIT_MOVE_XYZ': 0x4A,
    'EDIT_EYELID_ANIM': 0x4B,
    'EDIT_INSTRUMENT_ITEM': 0x4C,
    'EDIT_MOTION_LOOP': 0x4D,
    'EDIT_EXPRESSION': 0x4E,
    'EDIT_EYE_ANIM': 0x4F,
    'EDIT_MOUTH_ANIM': 0x50,
    'EDIT_CAMERA': 0x51,
    'EDIT_MODE_SELECT': 0x52,
    'PV_END_FADEOUT': 0x53,
}


x_to_f_mouths = {
    4:34,
    5:35,
    6:36,
    7:37,
    8:38,
    9:39,
    10:4,
    11:5,
    12:6,
    13:7,
    14:8,
    15:9,
    16:10,
    17:11,
    18:12,
    19:13,
    20:14,
    21:15,
    22:16,
    23:17,
    24:18,
    25:19,
    26:20,
    27:21,
    28:22,
    29:40,
    30:41,
    31:42
}

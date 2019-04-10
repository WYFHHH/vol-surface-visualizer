# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class Subscribe(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSubscribe(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Subscribe()
        x.Init(buf, n + offset)
        return x

    # Subscribe
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Subscribe
    def Request(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Subscribe
    def Topic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Subscribe
    def Match(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Subscribe
    def GetRetained(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def SubscribeStart(builder): builder.StartObject(4)
def SubscribeAddRequest(builder, request): builder.PrependUint64Slot(0, request, 0)
def SubscribeAddTopic(builder, topic): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(topic), 0)
def SubscribeAddMatch(builder, match): builder.PrependUint8Slot(2, match, 0)
def SubscribeAddGetRetained(builder, getRetained): builder.PrependBoolSlot(3, getRetained, 0)
def SubscribeEnd(builder): return builder.EndObject()

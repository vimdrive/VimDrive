import pynvim

@pynvim.plugin
class VimDrive:
    def __init__(self, nvim):
        self.nvim = nvim


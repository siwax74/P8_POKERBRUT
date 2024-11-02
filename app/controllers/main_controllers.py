######################################################################################################################
############################################### MAIN_CONTROLLERS.PY ##################################################
######################################################################################################################

from app.controllers.frame_controller import FrameController, FrameControllerInit


class MainController:
    def __init__(self, root):
        self.root = root

    def run(self):
        frame_controller_init = FrameControllerInit(self.root)
        frame_controller_init.init_param_main_view()
        frame_controller = FrameController(frame_controller_init)
        frame_controller.load_main_view()
        self.root.mainloop()

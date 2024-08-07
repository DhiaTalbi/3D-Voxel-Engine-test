import numpy as np


class BaseMesh():
    def __init__(self):
        #OpenGL Context
        self.ctx = None
        #Shader Program
        self.program = None
        #Vertex Buffer Data Type Format: '3f 3f'
        self.vbo_format = None
        #Attributes Names According to The Format: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        #Vertex Array Object
        self.vao = None 

    def get_vertex_data(self) -> np.array : ...

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors = True )
        return vao
    
    def render(self):
        self.vao.render()
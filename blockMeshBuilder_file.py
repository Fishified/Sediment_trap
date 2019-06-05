import blockMeshBuilder as block

x_axis=[0,0.275,0.3,0.55]
y_axis=[0,0.075]
z_axis=[0,0.05,0.065,0.075,0.175]

x_sizes=[0.002,0.002,0.002]
y_sizes=[0.002]
z_sizes=[0.002,0.002,0.002,0.002]

gr_x=[1,1,1]
gr_y=[1]
gr_z=[1,1,1,1]

domain=block.Domain(x_axis,
					y_axis,
					z_axis,
					x_sizes,
					y_sizes,
					z_sizes,
					gr_x,
					gr_y,
					gr_z)
        
a=block.Render(domain)
a.show()






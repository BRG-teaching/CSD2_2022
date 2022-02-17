import os
import compas

from compas.datastructures import Mesh, mesh_bounding_box_xy
from compas.geometry import Vector, Frame, Scale
from compas_rhino.artists import MeshArtist

HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'sessions', 'bm_vertical_equilibrium', 'simple_tripod.rv2')
FILE_O = os.path.join(HERE, 'data', 'form.json')

session = compas.json_load(FILE_I)

form = Mesh.from_data(session['data']['form'])

'''
form.to_json(FILE_O)

artist = MeshArtist(form, layer="RV2::Mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
'''

#------------delete extra faces------------
mesh = form
delete_faces =[]

for fkey in mesh.faces():
    if len(mesh.face_vertices(fkey)) > 4:
        delete_faces.append(fkey)

for fkey in delete_faces:       
    mesh.delete_face(fkey)
    #mesh.cull_vertices()
    mesh.remove_unused_vertices()

#----------scale up the form---------------

box_points = mesh_bounding_box_xy(mesh)
base_mesh = mesh.from_points(box_points)
centroid = base_mesh.centroid()

print (centroid)
frame = Frame(centroid,Vector(1,0,0),Vector(0,1,0))

S = Scale.from_factors([100, 100, 100], frame)
mesh.transform(S)

mesh.to_json(FILE_O)

artist = MeshArtist(mesh, layer="RV2::New_Scaled_Mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
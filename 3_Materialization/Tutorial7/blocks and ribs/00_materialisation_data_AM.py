import os
import compas

from compas.datastructures import Mesh, mesh_bounding_box_xy
from compas.geometry import Vector, Frame, Scale
from compas_rhino.artists import MeshArtist

HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'sessions', 'bm_vertical_equilibrium', 'simple_tripod.rv2')
FILE_O1 = os.path.join(HERE, 'data', 'form.json')
FILE_O2 = os.path.join(HERE, 'data', 'scaled_form.json')

session = compas.json_load(FILE_I)

mesh = Mesh.from_data(session['data']['form'])

#------------to delete extra faces(less than 4 edges) if subdivided with catmulclark or other weird subdivision that connects the mesh with the ground------------
delete_faces =[]

for fkey in mesh.faces():
    if len(mesh.face_vertices(fkey)) > 4:
        delete_faces.append(fkey)

for fkey in delete_faces:       
    mesh.delete_face(fkey)
    #scaled_mesh.cull_vertices()
    mesh.remove_unused_vertices()

#----------scale up the form if needed---------------
scaled_mesh = mesh.copy()

box_points = mesh_bounding_box_xy(scaled_mesh)
base_mesh = scaled_mesh.from_points(box_points)
centroid = base_mesh.centroid()
#print (centroid)
frame = Frame(centroid,Vector(1,0,0),Vector(0,1,0))

S = Scale.from_factors([100, 100, 100], frame)
scaled_mesh.transform(S)

mesh.to_json(FILE_O1)
scaled_mesh.to_json(FILE_O2)

artist = MeshArtist(mesh, layer="RV2::Initial_Mesh")
artist.clear_layer()
artist.draw_faces(join_faces=True)
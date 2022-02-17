import math, compas
import os
from compas.datastructures import Mesh
from compas.geometry._core.distance import distance_point_point
from compas_rhino.artists import MeshArtist
from compas.geometry import Vector
from compas.geometry import add_vectors
from compas.geometry import angle_vectors
from compas.geometry import trimesh_remesh

HERE = os.path.dirname(__file__)

FILE_I = os.path.join(HERE, 'data', 'scaled_form.json')
FILE_O_1 = os.path.join(HERE, 'data', 'Ribs_Mesh.json')
FILE_O_2 = os.path.join(HERE, 'data', 'Caps_Mesh.json')

form = Mesh.from_json(FILE_I)
form_cap = form.copy()
form_cap.clear()


def orientation(mesh):
    for vkey in mesh.vertices():
        print(vkey, mesh.vertex_normal(vkey))

    artist = MeshArtist(mesh, layer="RV2::Normals")
    artist.clear_layer()
    artist.draw_edges()
    artist.draw_vertexnormals(scale=1)


def math_map_list(values, toMin=0, toMax=1):
    """
    Maps the values of a list from a minimum value to a maximum value.
    ----------
    values : list to be mapped
    ----------
    toMin : minimum value of the list's target range (default = 0)
    toMax : maximum value of the list's target range (default = 1)
    """
    minValue = min(values)
    maxValue = max(values)
    delta = maxValue - minValue
    deltaTarget = toMax - toMin
    newValues = [toMin +(value-minValue)*deltaTarget/delta for value in values]
    return newValues


def ribs_mesh(mesh, meshcap, fkey, ratio, keep_original, doCap=True):
    
    centroid = mesh.face_centroid(fkey)
    centroid_vector = Vector(*centroid)
    normal = mesh.face_normal(fkey)
    normal_vector = Vector(*normal)

    face_verts = mesh.face_vertices(fkey)
    new_verts = []
    new_cap_verts = []
    cap_faces = []
    
    if keep_original == False:
        for v in face_verts:
            v_coords = mesh.vertex_coordinates(v)
            v_vector = Vector(*v_coords)
            vert_to_cent = centroid_vector - v_vector
            vert_to_cent *= ratio
            new_vertex = v_vector + vert_to_cent + normal_vector
            x, y, z = new_vertex
            new_verts.append(mesh.add_vertex(x=x, y=y, z=z))
            if doCap == True:
                new_cap_verts.append(meshcap.add_vertex(x=x, y=y, z=z))
 
        new_keys = []
        for i, v in enumerate(face_verts):
            next_v = face_verts[(i+1) % len(face_verts)]
            new_v = new_verts[i]
            next_new_v = new_verts[(i+1) % len(face_verts)]
            new_face_key = mesh.add_face([v, next_v, next_new_v, new_v])
            new_keys.append(new_face_key)

        if doCap:
            top_face_key = meshcap.add_face(new_cap_verts)
            new_keys.append(top_face_key)
            cap_faces.append(top_face_key)

        mesh.delete_face(fkey)
        return new_keys, cap_faces
    
    else:
        return fkey, []


#-----------z positions----------------------------------------------------------

# analyse z positions of faces
z_positions = []
for key in form.faces():

    z_positions.append( form.face_center(key)[2])

#z_positions = math_map_list(z_positions, 0, 1)

#Dont Subdivide when below 0.15 (=15%) or if the face is a boundary face
keep_orig = [False] * len(z_positions)

new_z_pos = math_map_list(z_positions, 0, 1)

for i in range(len(new_z_pos)):
    if new_z_pos[i] < 0.05:
        z_positions[i] = 0
        keep_orig[i]=True
    if new_z_pos[i] > 0.9:
        z_positions[i] = max(z_positions)

faces = form.face
fkeys = list(form.faces())
for i, (fkey, keep) in enumerate(zip(form.faces(), keep_orig)):
    num = len(form.face_neighbors(fkey))
    if len(form.face_neighbors(fkey)) <= 3:
        keep_orig[i] = True


# ratio of frame offset depending on z position:
ratios = []
min_edges = []
max_edges =[]

for fkey in form.faces():
    edges = form.face_halfedges(fkey)
    lengths=[]
    for e in edges:
        len_e = len(e)
        lengths.append(len_e)
    min_e = min(lengths)
    max_e = max(lengths)
    min_edges.append(min_e)
    max_edges.append(max_e)

ratios = []

for z_pos, min_edge, max_edge in zip(z_positions, min_edges, max_edges):
    ratio = (z_pos / max_edge) * (min_edge /2)
    ratios.append(ratio)

remaped_ratios = math_map_list(ratios, 0.4, 0.1)


# show orientation of normals---------------------------------------------------------------
normals_mesh = Mesh.from_json(FILE_I)
orientation(normals_mesh)

#-----------parametric subdivision----------------------------------------------------------

#parametric subdivision based on the analyses
# no frames at the bottom, smaller frames at the middle, bigger frames at the top

fkeys = list(form.faces())
print (len(fkeys))


for f, rat, keep in zip(fkeys, remaped_ratios, keep_orig):
    new_ribs, new_caps =  ribs_mesh(form, form_cap, f, rat, keep)


artist = MeshArtist(form, layer="ribs")
artist.clear_layer()
artist.draw_faces(join_faces=True)

artist1 = MeshArtist(form_cap, layer="caps")
artist1.clear_layer()
artist1.draw_faces(join_faces=True)

form.to_json(FILE_O_1)
form_cap.to_json(FILE_O_2)

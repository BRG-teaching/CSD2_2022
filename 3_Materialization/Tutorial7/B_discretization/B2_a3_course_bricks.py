# ==============================================================================
#Imports
# ==============================================================================
import os
import json

from compas.datastructures import Mesh
from compas_rhino.artists import MeshArtist
from compas.geometry import subtract_vectors, scale_vector, add_vectors
# ==============================================================================
#Load data
# ==============================================================================

HERE = os.path.dirname(__file__)
FILE_I = os.path.join(HERE, 'data', 'brick_pattern_data.json')

mesh = Mesh.from_json(FILE_I)

# ==============================================================================
#Params
# ==============================================================================

offset_value = 0.1

# ==============================================================================
#Helper functions
# ==============================================================================

def check_neighbors_and_offset_vector(mesh,vkey,fkey,offset_value):
    v_neighbors = mesh.vertex_neighborhood(vkey)

    v_descendant = mesh.face_vertex_descendant(fkey,vkey,n=1)
    v_ancestor = mesh.face_vertex_ancestor(fkey,vkey,n=1)

    g = None
    for v in v_neighbors:
        if v != v_descendant and v != v_ancestor:
            g = v

    g_xyz = mesh.vertex_coordinates(g,axes='xyz')
    v_xyz = mesh.vertex_coordinates(vkey,axes='xyz')
    vector = subtract_vectors(g_xyz, v_xyz)
    offset_coordinates = add_vectors(v_xyz, scale_vector(vector,offset_value))

    return offset_coordinates

def calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value):
    v_xyz = mesh.vertex_coordinates(vkey)
    if order =="ancestor":
        v_neighbor = mesh.face_vertex_ancestor(fkey,vkey,n=1)
        v2_xyz = mesh.vertex_coordinates(v_neighbor,axes='xyz')

    elif order =="descendant":
        v_neighbor = mesh.face_vertex_descendant(fkey,vkey,n=1)
        v2_xyz = mesh.vertex_coordinates(v_neighbor,axes='xyz')

    vector = subtract_vectors(v2_xyz, v_xyz)
    offset_coordinates = add_vectors(v_xyz, scale_vector(vector,offset_value))

    return offset_coordinates

#================================================================
#hexagonal brick pattern
#================================================================
#visually identify face index along south and north boundary.
# This can be automated, however for this exercise we will do it manually

south_boundary_faces = (0,1,2,3,4,5)
north_boundary_faces = (12,13,14,15,16,17)

#create list to store newly created hexaconal pattern meshes
hexagonal_meshes = []

#South boundary
for fkey in (south_boundary_faces):
    tess_mesh = Mesh()

    for i,vkey in enumerate(mesh.face_vertices(fkey)):

        if i==0:
            v_xyz = mesh.vertex_coordinates(vkey)
            a = tess_mesh.add_vertex(x=v_xyz[0],y=v_xyz[1],z=v_xyz[2])

        elif i==1:
            v_xyz = mesh.vertex_coordinates(vkey)
            b = tess_mesh.add_vertex(x=v_xyz[0], y=v_xyz[1],z=v_xyz[2])

        elif i==2:
            v_xyz = mesh.vertex_coordinates(vkey)
            c = tess_mesh.add_vertex(x=v_xyz[0], y=v_xyz[1],z=v_xyz[2])

        elif i==3:
            order = "ancestor"
            offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
            d = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])


        elif i == 4:
            offset_xyz = check_neighbors_and_offset_vector(mesh,vkey,fkey,offset_value)
            e = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])

        elif i == 5:
            order = "descendant"
            offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
            f = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])

    tess_mesh.add_face([0,1,2,3,4,5])
    hexagonal_meshes.append(tess_mesh)

#north boundary
for fkey in north_boundary_faces:
    tess_mesh = Mesh()

    for i,vkey in enumerate(mesh.face_vertices(fkey)):
        if i==0:
            order = "ancestor"
            offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
            a = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
        elif i==1:
            offset_xyz = check_neighbors_and_offset_vector(mesh,vkey,fkey,offset_value)
            b = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
        elif i==2:
            order = "descendant"
            offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
            c = tess_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
        elif i==3:
            v_xyz = mesh.vertex_coordinates(vkey)
            d = tess_mesh.add_vertex(x=v_xyz[0], y=v_xyz[1],z=v_xyz[2])

        elif i==4:
            v_xyz = mesh.vertex_coordinates(vkey)
            e = tess_mesh.add_vertex(x=v_xyz[0], y=v_xyz[1],z=v_xyz[2])

        elif i==5:
            v_xyz = mesh.vertex_coordinates(vkey)
            f = tess_mesh.add_vertex(x=v_xyz[0], y=v_xyz[1],z=v_xyz[2])

    tess_mesh.add_face([0,1,2,3,4,5])
    hexagonal_meshes.append(tess_mesh)

#identify full bricks/middle faces
faces = list(fkey for fkey in mesh.faces())
boundary_faces = south_boundary_faces + north_boundary_faces
middle_faces = set(faces) ^ set(boundary_faces)
for fkey in middle_faces:
    if len(mesh.face_vertices(fkey))==6:
        middle_mesh = Mesh()
        new_vertices = []
        for i,vkey in enumerate(mesh.face_vertices(fkey)):

            if i==0:
                order = "ancestor"
                offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
                a = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(a)


            elif i==1:
                offset_xyz = check_neighbors_and_offset_vector(mesh,vkey,fkey,offset_value)
                b = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(b)

            elif i==2:
                order = "descendant"
                offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
                c = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(c)
            elif i==3:
                order = "ancestor"
                offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
                d = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(d)

            elif i == 4:
                offset_xyz = check_neighbors_and_offset_vector(mesh,vkey,fkey,offset_value)
                e = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(e)

            elif i == 5:
                order = "descendant"
                offset_xyz = calc_vector_and_offset_vertex(mesh,vkey,fkey,order,offset_value)
                f = middle_mesh.add_vertex(x=offset_xyz[0], y=offset_xyz[1],z=offset_xyz[2])
                new_vertices.append(f)

        middle_mesh.add_face(new_vertices)
        hexagonal_meshes.append(middle_mesh)

#================================================
#Visualize
#================================================
artist = MeshArtist(None, layer="CSD2::hexagonal_tess::boundary")
artist.clear_layer()

for mesh in hexagonal_meshes:
    artist = MeshArtist(mesh, layer="CSD2::hexagonal_tess::boundary")
    artist.draw_faces()
    artist.draw_vertices()
    artist.draw_vertexlabels()
    artist.draw_edges()
    artist.redraw()

if __name__ == '__main__':
    pass

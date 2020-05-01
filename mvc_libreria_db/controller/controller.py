from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """

    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***********************
    * General controllers *
    ***********************
    """   

    def main_menu(self):
        o = '0'
        while o != '6':
            self.view.main_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.dir_menu()
            elif o == '2':
                self.autor_menu()
            elif o == '3':
                self.libro_menu()
            elif o == '4':
                self.usuarios_menu()
            elif o == '5':
                self.prestamo_menu()
            elif o == '6':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals
    
    """
    ********************
    * General for dir's *
    ********************
    """

    def dir_menu(self):
        o = '0'
        while o != '13':
            self.view.dir_menu()
            self.view.option('13')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_zip() 
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            ############ DIRECCIONES ############3
            elif o == '7':
                self.create_dir()
            elif o == '8':
                self.read_a_dir()
            elif o == '9':
                self.read_all_dirs()
            elif o == '10':
                self.read_dirs_cp()
            elif o == '11':
                self.update_dir()
            elif o == '12':
                self.delete_dir()
            elif o == '13':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city,state] 
    
    def create_zip(self):
        self.view.ask('CP: ')
        cp = input()
        ciudad, estado = self.ask_zip()
        out = self.model.create_zip(cp,ciudad,estado)
        if out == True:
            self.view.ok(cp, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('El CP esta repetido')
            else:
                self.view.error('No se pudo agregar el CP')
        return
    
    def read_zip(self):
        self.view.ask('CP: ')
        i_cp = input()
        cp = self.model.read_zip(i_cp)
        if type(cp) == tuple:
            self.view.show_zip_header('Datos del CP  '+i_cp+' ')
            self.view.show_a_zip(cp)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if cp == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Hay un problema al leer el CP')
        return
    
    def read_all_zips(self):
        cps = self.model.read_all_zips()
        if type(cps) ==  list:
            self.view.show_zip_header(' Todos los CPs ')
            for cp in cps:
                self.view.show_a_zip(cp)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Hay un problema al leer los CPs ')
        
    
    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        ciudad = input()
        cps = self.model.read_zips_city(ciudad)
        if type(cps) == list:
            self.view.show_zip_header('CP para la ciudad de  '+ciudad+' ')
            for cp in cps:
                self.view.show_a_zip(cp)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('Hay un problema al leer los CPs ')
        return
    

    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_cp = input()
        cp = self.model.read_zip(i_cp)
        if type(cp) == tuple:
            self.view.show_zip_header(' Datos del CP '+i_cp+' ')
            self.view.show_a_zip(cp)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if cp == None:
                self.view.error('El CP no existe')
            else:
                self.view.error('Hay un problema al leer el CP')
            return
        self.view.msg(' Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals =self.ask_zip()
        fields, vals = self.update_lists(['ciudad','estado'], whole_vals)
        vals.append(i_cp)
        vals = tuple(vals)
        out = self.model.update_zip(fields,vals)
        if out == True:
            self.view.ok(i_cp, 'actualizo')
        else: 
            self.view.error('No se pudo actualizar el CP')
        return

    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_cp = input()
        count = self.model.delete_zip(i_cp)
        if count != 0:
            self.view.ok(i_cp, 'borro')
        else:
            if count == 0:
                self.view.error('El CP no exite')
            else:
                self.view.error('Problema al borrar el CP')
        return

    """ 
    ***************************
    * Controllers for dir's   *
    ***************************
    """
    
    def ask_dir(self):
        self.view.ask('Calle: ')
        calle = input()
        self.view.ask('Colonia: ')
        colonia = input()
        self.view.ask('Num Ext: ')
        n_ext = input()
        self.view.ask('Num Int: ')
        n_int = input()
        self.view.ask('CP: ')
        cp = input()
        return [calle, colonia, n_ext, n_int, cp] 

    
    def create_dir(self):
        calle, colonia, n_ext, n_int, cp = self.ask_dir()
        out = self.model.create_dir(calle, colonia, n_ext, n_int, cp)
        if out == True:
            self.view.ok(calle+' #'+n_ext +' Colonia: '+ colonia+' ',' agrego')
        else:
            self.view.error('No se pudo agregar el producto')
        return
    
    def read_a_dir(self):
        self.view.ask('ID Dir: ')
        i_dir = input()
        dir = self.model.read_dir(i_dir)
        if type(dir) == tuple:
            self.view.show_dir_header('Datos de la dirección  '+i_dir+' ')
            self.view.show_a_dir(dir)
            self.view.show_dir_midder()
            self.view.show_dir_footer()
        else:
            if dir == None:
                self.view.error('El ID de la dirección no existe')
            else:
                self.view.error('Hay un problema al leer la dirección')
        return


    def read_all_dirs(self):
        dirs = self.model.read_all_dir()
        if type(dirs) ==  list:
            self.view.show_dir_header(' Todas las direcciones ')
            for dir in dirs:
                self.view.show_a_dir(dir)
            self.view.show_dir_midder()
            self.view.show_dir_footer()
        else:
            self.view.error('Hay un problema al leer las direcciones ')
        

    def read_dirs_cp(self):
        self.view.ask('Cp: ')
        cp = input()
        dirs = self.model.read_dir_cps(cp)
        if type(dirs) == list:
            self.view.show_dir_header('Ciudades con el código postal:  '+cp+' ')
            for dir in dirs:
                self.view.show_a_dir(dir)
            self.view.show_dir_midder()
            self.view.show_dir_footer()
        else:
            self.view.error('Hay un problema al leer las direcciones con ese CP ')
        return

    
    def update_dir(self):
        self.view.ask('Dirección a modificar: ')
        i_dir = input()
        dir = self.model.read_dir(i_dir)
        if type(dir) == tuple:
            self.view.show_dir_header(' Datos de la dirección '+i_dir+' ')
            self.view.show_a_dir(dir)
            self.view.show_dir_midder()
            self.view.show_dir_footer()
        else:
            if dir == None:
                self.view.error('La id con esa dirección no existe')
            else:
                self.view.error('Hay un problema al leer esa dirección')
            return
        self.view.msg(' Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals =self.ask_dir()
        fields, vals = self.update_lists(['d_calle','d_col','d_numExt', 'd_numInt', 'd_cp'], whole_vals)
        vals.append(i_dir)
        vals = tuple(vals)
        out = self.model.update_dir(fields,vals)
        if out == True:
            self.view.ok(i_dir, 'actualizo')
        else: 
            self.view.error('No se pudo actualizar la dirección')
        return

    def delete_dir(self):
        self.view.ask('Dirección a borrar: ')
        i_dir = input()
        count = self.model.delete_dir(i_dir)
        if count != 0:
            self.view.ok(i_dir, 'borro')
        else:
            if count == 0:
                self.view.error('La dirección no existe')
            else:
                self.view.error('Problema al borrar la dirección')
        return

    """ 
    ***************************
    * Controllers for author's   *
    ***************************
    """


    def autor_menu(self):
        o = '0'
        while o != '7':
            self.view.autor_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_autor()
            elif o == '2':
                self.read_a_autor()
            elif o == '3':
                self.read_all_autors()
            elif o == '4':
                self.read_author_ap()
            elif o == '5':
                self.update_autor()
            elif o == '6':
                self.delete_autor()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    

    def ask_autor(self):
        self.view.ask('Nombre: ')
        a_nombre = input()
        self.view.ask('Apellido paterno: ')
        a_apellidoPat = input()
        self.view.ask('Apellido Materno: ')
        a_apellidoMat = input()
        return(a_nombre,a_apellidoPat,a_apellidoMat)
    
    def create_autor(self):
        a_nombre,a_apellidoPat,a_apellidoMat = self.ask_autor()
        out = self.model.create_autor(a_nombre,a_apellidoPat,a_apellidoMat)
        if out == True:
            self.view.ok(a_nombre+' '+a_apellidoPat+' '+a_apellidoMat, 'agrego')
        else:
            self.view.error('No se pudo agregar el autor')
        return
    
    def read_a_autor(self):
        self.view.ask('ID autor: ')    
        id_autor = input()
        autor = self.model.read_autor(id_autor)
        if type(autor) == tuple:
            self.view.show_autor_header('Datos del autor  '+id_autor+' ')
            self.view.show_a_autor(autor)
            self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            if autor == None:
                self.view.error('El autor no existe')
            else:
                self.view.error('Hay un problema al leer el autor')
        return
    
    def read_all_autors(self):
        autors = self.model.read_all_autors()
        if type(autors) == list:
            self.view.show_autor_header(' Todos los autores ')
            for autor in autors:
                self.view.show_a_autor(autor)
                self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            self.view.error('Problema al leer los autores')
        return
    

    def read_author_ap(self):
        self.view.ask('Apellido Paterno: ')
        ap = input()
        autores = self.model.read_author_ap(ap)
        if type(autores) == list:
            self.view.show_autor_header('Autores con el apellido paterno: '+ap+' ')
            for autor in autores:
                self.view.show_a_autor(autor)
                self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            self.view.error('Problema al leer los autores')
        return
    

    def update_autor(self):
        self.view.ask('ID del autor a modificar: ')
        id_autor = input()
        autor = self.model.read_autor(id_autor)
        if type(autor) == tuple:
            self.view.show_autor_header(' Datos del autor '+id_autor+ ' ')
            self.view.show_a_autor(autor)
            self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            if autor == None:
                self.view.error('El autor no existe')
            else:
                self.view.error('Problema al leer el autor')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_autor()
        fields, vals = self.update_lists(['a_nombre','a_apellidoPat','a_apellidoMat'], whole_vals)
        vals.append(id_autor)
        vals = tuple(vals)
        out = self.model.update_autor(fields,vals)
        if out == True:
            self.view.ok(id_autor, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el autor')
        return
    
    def delete_autor(self):
        self.view.ask('ID del autor a borrar: ')
        id_autor = input()
        count = self.model.delete_autor(id_autor)
        if count != 0:
            self.view.ok(id_autor, 'Borro')
        else:
            if count == 0:
                self.view.error('El autor no exite')
            else:
                self.view.error('Prblema al borrar el autor')
        return
    
    """ 
    ***************************
    * Controllers for libros  *
    ***************************
    """

    def libro_menu(self):
        o = '0'
        while o != '7':
            self.view.libro_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_libro()
            elif o == '2':
                self.read_a_libro()
            elif o == '3':
                self.read_all_libros()
            elif o == '4':
                self.read_libro_nombre()
            elif o == '5':
                self.update_libro()
            elif o == '6':
                self.delete_libro()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_libro(self):
        self.view.ask('Nombre: ')
        l_nombre = input()
        self.view.ask('Cantidad: ')
        l_cantidad = input()
        self.view.ask('Edición: ')
        l_edicion = input()
        self.view.ask('Autor: ')
        l_id_autor = input()
        return [l_nombre, l_cantidad,l_edicion,l_id_autor]
    
    def create_libro(self):
        l_nombre, l_cantidad, l_edicion, l_id_autor = self.ask_libro()
        out = self.model.create_libro(l_nombre, l_cantidad, l_edicion, l_id_autor)
        if out == True:
            self.view.ok(l_nombre+' '+' Edición: '+l_edicion,'agrego')
        else:
            self.view.error('No se pudo agregar el libro')
        return
    
    def read_a_libro(self):
        self.view.ask('ID libro: ')
        id_libro = input()
        libro = self.model.read_book(id_libro)
        if type(libro) == tuple:
            self.view.show_libro_header('Datos del libro  '+id_libro+' ')
            self.view.show_a_libro(libro)
            self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
            if libro == None:
                self.view.error('El libro no existe')
            else:
                self.view.error('Hay un problema al leer el libro')
        return
    
    def read_all_libros(self):
        libros = self.model.read_all_books()
        if type(libros) ==  list:
            self.view.show_libro_header(' Todos los libros ')
            for libro in libros:
                self.view.show_a_libro(libro)
                self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
            self.view.error('Hay un problema al leer los libros ')
        
    
    def read_libro_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        libros = self.model.read_book_name(nombre)
        if type(libros) == list:
            self.view.show_libro_header('Libros con el nombre '+nombre+' ')
            for libro in libros:
                self.view.show_a_libro(libro)
                self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
            self.view.error('Problema al leer los libros')
        return
    
    def update_libro(self):
        self.view.ask('Libro a modificar: ')
        id_libro = input()
        libro = self.model.read_book(id_libro)
        if type(libro) == tuple:
            self.view.show_libro_header(' Datos del libro '+id_libro+ ' ')
            self.view.show_a_libro(libro)
            self.view.show_libro_midder()
            self.view.show_libro_footer()
        else:
            if libro == None:
                self.view.error('El libro no existe')
            else:
                self.view.error('Problema al leer el libro')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_libro()
        fields, vals = self.update_lists(['l_nombre','l_cantidad','l_edicion','l_id_autor'], whole_vals)
        vals.append(id_libro)
        vals = tuple(vals)
        out = self.model.update_book(fields,vals)
        if out == True:
            self.view.ok(id_libro, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el libro')
        return
    
    def delete_libro(self):
        self.view.ask('ID de libro a borrar: ')
        id_libro = input()
        count = self.model.delete_book(id_libro)
        if count != 0:
            self.view.ok(id_libro, 'Borro')
        else:
            if count == 0:
                self.view.error('El libro no exite')
            else:
                self.view.error('Prblema al borrar el libro')
        return
    
    """ 
    *****************************
    * Controllers for usuarios  *
    *****************************
    """

    def usuarios_menu(self):
        o = '0'
        while o != '7':
            self.view.usuarios_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_a_user()
            elif o == '3':
                self.read_all_users()
            elif o == '4':
                self.read_user_ap()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido Materno: ')
        sname2 = input()
        self.view.ask('Telefono: ')
        telefono = input()
        self.view.ask('Correo: ')
        correo = input() 
        self.view.ask('ID de la dirección: ')
        id_dir = input() 
        self.view.ask('CP: ')
        cp = input() 
        return(name,sname1,sname2,telefono,correo,id_dir,cp)
    

    def create_user(self):
        name,sname1,sname2,telefono,correo,id_dir,cp = self.ask_user()
        out = self.model.create_user(name,sname1,sname2,telefono,correo,id_dir,cp)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else:
            self.view.error('No se pudo agregar el usuario')
        return
    
    def read_a_user(self):
        self.view.ask('ID usuario: ')    
        id_usuario = input()
        usuario = self.model.read_user(id_usuario)
        if type(usuario) == tuple:
            self.view.show_user_header('Datos del cliente  '+id_usuario+' ')
            self.view.show_a_user(usuario)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if usuario == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Hay un problema al leer el usuario')
        return
    

    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header(' Todos los usuarios ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Problema al leer los usuarios')
        return
    
    def read_user_ap(self):
        self.view.ask('Apellido paterno: ')
        ap = input()
        users = self.model.read_user_ap(ap)
        if type(users) == list:
            self.view.show_user_header('Usuarios con el apellido paterno '+ap+' ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Problema al leer los usuarios')
        return
    
    def update_user(self):
        self.view.ask('ID del usuario a modificar: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del usuario '+id_user+ ' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Problema al leer el usuario')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['u_nombre','u_apellidopat','u_apellidomat','u_tel','correo','u_id_dir','u_cp'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields,vals)
        if out == True:
            self.view.ok(id_user, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el usuario')
        return
    
    def delete_user(self):
        self.view.ask('ID del usuario a borrar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'Borro')
        else:
            if count == 0:
                self.view.error('El usuario no exite')
            else:
                self.view.error('Prblema al borrar el usuario')
        return
    
    """ 
    ****************************
    * Controllers for prestamo *
    ****************************
    """ 

    def prestamo_menu(self):
        o = '0'
        while o != '14':
            self.view.prestamo_menu()
            self.view.option('14')
            o = input()
            if o == '1':
                self.create_prestamo()
            elif o == '2':
                self.read_prestamo()
            elif o == '3':
                self.read_all_prestamos()
            elif o == '4':
                self.read_prestamo_user()
            elif o == '5':
                self.update_prestamo()
            elif o == '6':
                self.delete_prestamo()
            elif o == '7':
                self.create_details_prestamo()
            elif o == '8':
                self.add_prestamo_details()
            elif o == '9':
                self.read_detalle_prestamo()
            elif o == '10':
                self.read_all_details_prestamos()
            elif o == '11':
                self.read_details_prestamo_book()
            elif o == '12':
                self.update_details_prestamo()
            elif o == '13':
                self.delete_details_prestamo()
        
            elif o == '14':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_prestamo(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        self.view.ask('Fecha de devolución: ')
        d_date = input()
        self.view.ask('Adeudo: ')
        adeudo = input()
        return('',d_date,adeudo,id_user)



    def create_prestamo(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        self.view.ask('Fecha de devolución: ')
        d_date = input()
        p_adeudo = 0.0
        today = date.today()
        p_date = today.strftime('%y-%m-%d')
        id_prestamo = self.model.create_prestamo(p_date, d_date, p_adeudo, id_user)
        if type(id_prestamo) == int:
            self.view.ok(id_prestamo,'agrego')
            prestamo = self.model.read_prestamo(id_prestamo)
            self.view.show_a_prestamo(prestamo)
            return prestamo
        else:
            self.view.error('No se pudo crear el prestamo')
        return

    
    def read_prestamo(self):
        self.view.ask('ID prestamo: ')    
        id_prestamo = input()
        prestamo = self.model.read_prestamo(id_prestamo)
        if type(prestamo) == tuple:
            self.view.show_prestamo_header('Datos del prestamo  '+id_prestamo+' ')
            self.view.show_a_prestamo(prestamo)
            self.view.show_prestamo_adeudo(prestamo)
            self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            if prestamo == None:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Hay un problema al leer el prestamo')
        return
    
    def read_all_prestamos(self):
        prestamos = self.model.read_all_prestamos()
        if type(prestamos) == list:
            self.view.show_prestamo_header(' Todos los prestamos ')
            for prestamo in prestamos:
                self.view.show_a_prestamo(prestamo)
                self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            self.view.error('Problema al leer los prestamos')
        return
    
    def read_prestamo_user(self):
        self.view.ask('ID del usuario: ')
        id_user = input()
        prestamos = self.model.read_prestamo_user(id_user)
        if type(prestamos) == list:
            self.view.show_prestamo_header('Prestamos del usario '+id_user+' ')
            for prestamo in prestamos:
                self.view.show_a_prestamo(prestamo)
                self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            self.view.error('Problema al leer los prestamos')
        return
    

    def update_prestamo(self):
        self.view.ask('ID del prestamo a modificar: ')
        id_prestamo = input()
        prestamo = self.model.read_prestamo(id_prestamo)
        if type(prestamo) == tuple:
            self.view.show_prestamo_header(' Datos del prestamo '+id_prestamo+ ' ')
            self.view.show_a_prestamo(prestamo)
            self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            if prestamo == None:
                self.view.error('El prestamo no existe')
            else:
                self.view.error('Problema al leer el prestamo')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_prestamo()
        fields, vals = self.update_lists(['pF_prestamo','pF_devolu','p_adeudo','p_id_usuario'], whole_vals)
        vals.append(id_prestamo)
        vals = tuple(vals)
        out = self.model.update_prestamo(fields,vals)
        if out == True:
            self.view.ok(id_prestamo, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el prestamo')
        return
    
    def delete_prestamo(self):
        self.view.ask('ID del prestamo a borrar: ')
        id_prestamo = input()
        count = self.model.delete_prestamo(id_prestamo)
        if count != 0:
            self.view.ok(id_prestamo, 'Borro')
        else:
            if count == 0:
                self.view.error('El prestamo no exite')
            else:
                self.view.error('Problema al borrar el prestamo')
        return

    """ 
    ************************************
    * Controllers for prestamo details *
    ************************************
    """ 
    def ask_dprestamo(self):
        self.view.ask('ID del libro: ')
        did_libro = input()
        self.view.ask('Cantidad: ')
        d_cantidad = input()
        self.view.ask('Adeudo total: ')
        d_adeudoTotal = input()
        return(did_libro, d_cantidad, d_adeudoTotal)
        


    def create_details_prestamo(self):
        pd_total = 0.0
        self.view.ask('ID libro: ')
        id_libro = input()
        self.view.ask('ID prestamo: ')
        id_prestamo = input()
        if id_libro != '':
            libro = self.model.read_book(id_libro)
            if type(libro) == tuple:
                self.view.show_libro_header(' Datos del libro '+id_libro+' ')
                self.view.show_a_libro(libro)
                self.view.show_libro_footer()
                self.view.ask('Cantidad: ')
                pd_amount = int(input())
                self.view.ask('Dias de prestamo: ')
                pd_dias = int(input())

                pd_total = pd_amount*pd_dias*5
                out = self.model.create_details_prestamo(id_prestamo, id_libro,pd_amount, pd_total)
                if out == True:
                    self.view.ok(libro[1]+' Edicion: '+libro[3], 'agrego al prestamo')
                else:
                    if out.errno == 1062:
                        self.view.error(' El libro ya esta en el prestamo')
                    else:
                        self.view.error('No se pudo agregar el libro')
                    od_total = 0.0
            else:
                if libro == None:
                    self.view.error('El libro no existe')
                else:
                    self.view.error('Problema al leer el libro')
        return id_libro, pd_total
    

    def add_prestamo_details(self):
        prestamo = self.read_prestamo()
        if type(prestamo) == tuple:
            id_prestamo = prestamo[0]
            p_total = prestamo[3]
            id_libro = ' '
            while id_libro != '':
                self.view.msg('--- Agrega libros a la orden (deja vacio el id del producto para salir) ---')
                id_libro, pd_total = self.create_details_prestamo()
                p_total += pd_total
            self.model.update_prestamo(('p_total = %s',),(p_total,id_prestamo))
        return
    

    def read_detalle_prestamo(self):
        self.view.ask('ID detalle prestamo: ')    
        id_dPrestamo = input()
        dprestamo = self.model.read_detallesprestamo(id_dPrestamo)
        if type(dprestamo) == tuple:
            self.view.show_prestamo_details_header()
            self.view.show_a_prestamo_details(dprestamo)
            self.view.show_prestamo_details_footer()
        else:
            if dprestamo == None:
                self.view.error('El detalle del prestamo no existe')
            else:
                self.view.error('Hay un problema al leer el detalle del prestamo')
        return
    

    def read_all_details_prestamos(self):
        dprestamos = self.model.read_all_detallesprestamo()
        if type(dprestamos) == list:
            self.view.show_prestamo_header(' Todos los detalles de los prestamos ')
            for dprestamo in dprestamos:
                self.view.show_a_prestamo_details(dprestamo)
                self.view.show_prestamo_midder()
            self.view.show_prestamo_details_footer()
        else:
            self.view.error('Problema al leer los detalles de prestamos')
        return
    

    def read_details_prestamo_book(self):
        self.view.ask('ID del libro: ')
        id_libro = input()
        dprestamos = self.model.read_detalleprestamo_book(id_libro)
        if type(dprestamos) == list:
            self.view.show_prestamo_header('Detalles del prestamo del libro'+id_libro+' ')
            for dprestamo in dprestamos:
                self.view.show_a_prestamo_details(dprestamo)
                self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            self.view.error('Problema al leer los detalles de prestamos')
        return
    

    def update_details_prestamo(self):
        self.view.ask('ID del detalle de prestamo a modificar: ')
        id_dprestamo = input()
        dprestamo = self.model.read_detallesprestamo(id_dprestamo)
        if type(dprestamo) == tuple:
            self.view.show_prestamo_header(' Datos del detalle de prestamo '+id_dprestamo+ ' ')
            self.view.show_a_prestamo(dprestamo)
            self.view.show_prestamo_midder()
            self.view.show_prestamo_footer()
        else:
            if dprestamo == None:
                self.view.error('El detalle del prestamo no existe')
            else:
                self.view.error('Problema al leer el detalle del prestamo')
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_dprestamo()
        fields, vals = self.update_lists(['d_id_libro','d_cantidad','d_adeudoTotal'], whole_vals)
        vals.append(id_dprestamo)
        vals = tuple(vals)
        out = self.model.update_detalleprestamo(fields,vals)
        if out == True:
            self.view.ok(id_dprestamo, 'actualizo')
        else:
            self.view.error('Error no se pudo actualizar el detalle de prestamo')
        return
    
    def delete_details_prestamo(self):
        self.view.ask('ID del detalle de prestamo a borrar: ')
        id_dprestamo = input()
        count = self.model.delete_detalleprestamo(id_dprestamo)
        if count != 0:
            self.view.ok(id_dprestamo, 'Borro')
        else:
            if count == 0:
                self.view.error('El detalle de prestamo no exite')
            else:
                self.view.error('Problema al borrar el detalle de prestamo')
        return
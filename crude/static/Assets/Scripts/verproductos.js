 // Obtener los datos del localStorage
 const imagenSrc = localStorage.getItem('productoImagen');
 const titulo = localStorage.getItem('productoTitulo');
 const descripcion = localStorage.getItem('productoDescripcion');
 const precio = localStorage.getItem('productoPrecio');

 // Asignar los datos a los elementos HTML correspondientes
 document.getElementById('productoImagen').src = imagenSrc;
 document.getElementById('productoTitulo').innerText = titulo;
 document.getElementById('productoDescripcion').innerText = descripcion;
 document.getElementById('productoPrecio').innerText = precio;
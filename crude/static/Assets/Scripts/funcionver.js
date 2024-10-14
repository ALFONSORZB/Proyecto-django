function comprarProducto(button) {
    // Obtener el contenedor del producto
    const producto = button.parentElement;

    // Capturar la imagen, título y descripción
    const imagenSrc = producto.querySelector('img').src;
    const titulo = producto.querySelector('h3').innerText;
    const descripcion = producto.querySelector('p').innerText;
    const precio = producto.querySelector('h5').innerText;

    // Guardar estos datos en localStorage
    localStorage.setItem('productoImagen', imagenSrc);
    localStorage.setItem('productoTitulo', titulo);
    localStorage.setItem('productoDescripcion', descripcion);
    localStorage.setItem('productoPrecio', precio);

    // Redirigir a la página de compra
    window.location.href = 'compra_producto.html';
}

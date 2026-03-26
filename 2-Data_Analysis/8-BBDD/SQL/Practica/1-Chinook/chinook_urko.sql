--PRIMERA PARTE
--1. Obtén los clientes de Brasil
select * 
    from customers
    where country = 'Brazil';


--2. Obtén los empleados que son agentes de eventos
select * 
    from employees
    where title = 'Sales Support Agent';


--3. Obtén las canciones de ‘AC/DC’
select * 
    from tracks as trk 
        inner join albums as alb on alb.albumid = trk.albumid 
        inner join artists as art on art.artistid = alb.artistid
    where art.name = 'AC/DC';


--4.Obtén los campos de los clientes que no sean de USA: Nombrecompleto, ID, País
select concat(firstname, ' ', lastname) AS [Nombre Completo], customerid as ID, country as País
    from customers;


--5. Obtén los empleados que son agentes de ventas: Nombrecompleto, Dirección (Ciudad, Estado, País) y email
select concat(firstname, ' ', lastname) AS [Nombre Completo], concat(address, ' (', city, ', ', state, ', ', country, ')') as Dirección, email
    from employees
    where title = 'Sales Support Agent';



--6. Obtén una lista con los países no repetidos a los que se han emitido facturas
select distinct(billingcountry) 
    from invoices;



--7. Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno.
select state as Estado, count(customerid) as [Número de clientes]
    from customers
    where country = 'USA'
    group by Estado;



--8. Cuántos artículos tiene la factura 37
select sum(quantity) as [Número de facturas]
    from invoice_items
    where invoiceid = 37;



--9. Cuántas canciones tiene ‘AC/DC’
select sum(trk.trackid ) as [Núm. canciones]
    from tracks as trk 
        inner join albums as alb on alb.albumid = trk.albumid 
        inner join artists as art on art.artistid = alb.artistid
    where art.name = 'AC/DC';
    


--10. Cuántos artículos tiene cada factura
select invoiceid as Factura, sum(quantity) as [Número de facturas]
    from invoice_items
    group by Factura;
    


--11. Cuántas facturas hay de cada país
select inv.billingcountry as País, sum(inv_it.quantity) as [Número de facturas]
    from invoices as inv
        inner join invoice_items as inv_it on inv.invoiceid = inv_it.invoiceid
    group by País;




--12. Cuántas facturas ha habido en 2009 y 2011
select substring(inv.invoicedate, 1, 4) as Año, sum(inv_it.quantity) as [Número de facturas]
    from invoices as inv
        inner join invoice_items as inv_it on inv.invoiceid = inv_it.invoiceid
    where Año in ('2009','2011')
    group by Año;



--13. Cuántas facturas ha habido entre 2009 y 2011
select substring(inv.invoicedate, 1, 4) as Año, sum(inv_it.quantity) as [Número de facturas]
    from invoices as inv
        inner join invoice_items as inv_it on inv.invoiceid = inv_it.invoiceid
    where Año between '2009' and'2011'
    group by Año;



--14. Cuántos clientes hay de España y de Brasil
select country as País, count(customerid) as [Núm. Clientes]
    from customers
    where country in ('Brazil','Spain')
    group by country;



--15. Obtén las canciones que su título empieza por ‘You’
select name as Canciones 
    from tracks
    where name like 'You%';
    


--SEGUNDA PARTE
--1. Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la factura y el país de la factura
select distinct(inv.invoiceid) as [Id factura], cust.firstname || ' ' || cust.lastname as Nombre, substring(inv.invoicedate,1,10) as Fecha, inv.billingcountry as País
    from invoices as inv
        inner join invoice_items as inv_it on inv_it.invoiceid = inv.invoiceid
        inner join customers as cust on cust.customerid = inv.customerid
    where inv.billingcountry = 'Brazil';


--2. Obtén cada factura asociada a cada agente de ventas con su nombre completo
select distinct(inv.invoiceid) as [Id factura], emp.firstname || ' ' || emp.lastname as [Nombre de empleado]
    from invoices as inv
        inner join customers as cust on cust.customerid = inv.customerid
        inner join employees as emp on emp.employeeid = cust.supportrepid;



--3. Obtén el nombre del cliente, el país, el nombre del agente y el total
select concat(cust.firstname,' ',cust.lastname) as [Nombre de cliente], cust.country as País,
        concat(emp.firstname,' ',emp.lastname) as [Nombre de empleado],
        sum(inv.total)
    from customers as cust
        inner join employees as emp on emp.employeeid = cust.supportrepid
        inner join invoices as inv on inv.customerid = cust.customerid
        group by cust.customerid;



--4. Obtén cada artículo de la factura con el nombre de la canción
select inv_it.invoicelineid as Artículo, trk.name
    from invoice_items as inv_it
        inner join tracks as trk on trk.trackid = inv_it.trackid
    order by Artículo;
    



--5. Muestra todas las canciones con su nombre, formato, álbum y género
select trk.name as Nombre, mt.name as Formato, alb.title as Álbum, gen.name as Género
    from tracks as trk
        inner join media_types as mt on mt.mediatypeid = trk.mediatypeid
        inner join albums as alb on alb.albumid = trk.albumid
        inner join genres as gen on gen.genreid = trk.genreid
    order by trk.trackid;




--6. Cuántas canciones hay en cada playlist
select pl.name as Playlist, count(plt.trackid) as [Núm. canciones]
    from playlists as pl
        inner join playlist_track as plt on plt.playlistid = pl.playlistid
    group by pl.playlistid;




--7.Cuánto ha vendido cada empleado
select concat(emp.firstname,' ',emp.lastname) as [Nombre de empleado],
        sum(inv_it.quantity) as Cantidad, sum(inv.total) as [Total (€)]
    from employees as emp
        inner join customers as cust on cust.supportrepid = emp.employeeid
        inner join invoices as inv on inv.customerid = cust.customerid
        inner join invoice_items as inv_it on inv_it.invoiceid = inv.invoiceid
    group by emp.employeeid;
    



--8.¿Quién ha sido el agente de ventas que más ha vendido en 2009?
select concat(emp.firstname,' ',emp.lastname) as [Nombre de empleado],
        sum(inv_it.quantity) as Cantidad, sum(inv.total) as [Total (€)]
    from employees as emp
        inner join customers as cust on cust.supportrepid = emp.employeeid
        inner join invoices as inv on inv.customerid = cust.customerid
        inner join invoice_items as inv_it on inv_it.invoiceid = inv.invoiceid
    group by emp.employeeid
    order by Cantidad desc
    --order by [Total (€)] desc; -- Valen las dos opciones
    limit 1;




--9.¿Cuáles son los 3 grupos que más han vendido?
select art.name as [Artistas],
        sum(inv_it.quantity) as Cantidad, sum(inv_it.unitprice) as [Total (€)]
    from artists as art
        inner join albums as alb on alb.artistid = art.artistid
        inner join tracks as trk on trk.albumid = alb.albumid
        inner join invoice_items as inv_it on inv_it.trackid = trk.trackid
    group by art.artistid
    order by Cantidad desc
    --order by [Total (€)] desc; -- Valen las dos opciones
    limit 3;
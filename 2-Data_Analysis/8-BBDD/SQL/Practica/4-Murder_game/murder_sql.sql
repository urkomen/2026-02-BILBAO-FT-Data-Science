-- Primer vistazo
SELECT name 
  FROM sqlite_master
 where type = 'table';
 

-- Vemos cada tabla
select * from crime_scene_report;
select date as Fecha, type as Tipo, city as Ciudad, description as Detalles 
    from crime_scene_report
    where type = 'murder'
      and date = '20180115'
      and city = 'SQL City';
      




select * from drivers_license;
select * from facebook_event_checkin;
select * from get_fit_now_check_in;
select * from get_fit_now_member;
select * from income;
select * from interview;
select * from get_fit_now_member;
select * from person;
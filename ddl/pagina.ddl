BEGIN;
--
-- Create model Empleado
--
CREATE TABLE "EMPLEADO" ("id_empleado" varchar(6) NOT NULL PRIMARY KEY, "empl_fechacontrato" date NULL, "empl_cargo" varchar(24) NULL, "empl_sueldo" integer NOT NULL);
--
-- Create model Especie
--
CREATE TABLE "ESPECIE" ("id_especie" varchar(6) NOT NULL PRIMARY KEY, "espe_nombre" varchar(40) NULL, "espe_raza" varchar(40) NULL);
--
-- Create model Sede
--
CREATE TABLE "SEDE" ("id_sede" varchar(6) NOT NULL PRIMARY KEY, "sed_nombre" varchar(40) NULL, "sed_region" varchar(40) NULL, "sed_comuna" varchar(40) NULL, "sed_direccion" varchar(255) NULL, "sed_correo" varchar(100) NOT NULL UNIQUE, "sed_numero" varchar(15) NULL, "sed_capacidad" integer NOT NULL);
--
-- Create model Usuario
--
CREATE TABLE "USUARIO" ("id_usuario" varchar(6) NOT NULL PRIMARY KEY, "username" varchar(40) NULL, "password" varchar(40) NULL, "user_nombre" varchar(40) NULL, "user_apellido" varchar(40) NULL, "user_telefono" varchar(15) NULL, "user_correo" varchar(100) NOT NULL UNIQUE, "user_direccion" varchar(255) NULL, "user_fechanac" date NULL, "user_fechareg" date NULL, "user_rol" varchar(40) NULL);
--
-- Create model Mascota
--
CREATE TABLE "MASCOTA" ("id_mascota" varchar(6) NOT NULL PRIMARY KEY, "masc_historial" varchar(255) NULL, "masc_sexo" varchar(15) NULL, "masc_edad" varchar(3) NULL, "masc_nombre" varchar(40) NULL, "masc_descripcion" varchar(40) NULL, "masc_fechaintroduccion" date NULL, "masc_estado" varchar(40) NULL, "id_especie_id" varchar(6) NOT NULL REFERENCES "ESPECIE" ("id_especie") DEFERRABLE INITIALLY DEFERRED, "id_sede_id" varchar(6) NOT NULL REFERENCES "SEDE" ("id_sede") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Solicitud
--
CREATE TABLE "SOLICITUD" ("id_solicitud" varchar(6) NOT NULL PRIMARY KEY, "soli_descripcion" varchar(255) NULL, "soli_fecha" date NULL, "soli_comision" integer NOT NULL, "soli_estado" varchar(40) NULL, "id_empleado_id" varchar(6) NOT NULL REFERENCES "EMPLEADO" ("id_empleado") DEFERRABLE INITIALLY DEFERRED, "id_mascota_id" varchar(6) NOT NULL REFERENCES "MASCOTA" ("id_mascota") DEFERRABLE INITIALLY DEFERRED, "id_sede_id" varchar(6) NOT NULL REFERENCES "SEDE" ("id_sede") DEFERRABLE INITIALLY DEFERRED, "id_usuario_id" varchar(6) NOT NULL REFERENCES "USUARIO" ("id_usuario") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field id_usuario to empleado
--
CREATE TABLE "new__EMPLEADO" ("id_empleado" varchar(6) NOT NULL PRIMARY KEY, "empl_fechacontrato" date NULL, "empl_cargo" varchar(24) NULL, "empl_sueldo" integer NOT NULL, "id_usuario_id" varchar(6) NOT NULL REFERENCES "USUARIO" ("id_usuario") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__EMPLEADO" ("id_empleado", "empl_fechacontrato", "empl_cargo", "empl_sueldo", "id_usuario_id") SELECT "id_empleado", "empl_fechacontrato", "empl_cargo", "empl_sueldo", NULL FROM "EMPLEADO";
DROP TABLE "EMPLEADO";
ALTER TABLE "new__EMPLEADO" RENAME TO "EMPLEADO";
CREATE INDEX "MASCOTA_id_especie_id_898f621b" ON "MASCOTA" ("id_especie_id");
CREATE INDEX "MASCOTA_id_sede_id_97ef4699" ON "MASCOTA" ("id_sede_id");
CREATE INDEX "SOLICITUD_id_empleado_id_f5cc9f33" ON "SOLICITUD" ("id_empleado_id");
CREATE INDEX "SOLICITUD_id_mascota_id_8c69bd34" ON "SOLICITUD" ("id_mascota_id");
CREATE INDEX "SOLICITUD_id_sede_id_2593ed13" ON "SOLICITUD" ("id_sede_id");
CREATE INDEX "SOLICITUD_id_usuario_id_5c6672e5" ON "SOLICITUD" ("id_usuario_id");
CREATE INDEX "EMPLEADO_id_usuario_id_85a11084" ON "EMPLEADO" ("id_usuario_id");
--
-- Create model BlogPost
--
CREATE TABLE "BLOGPOST" ("id_post" varchar(100) NOT NULL PRIMARY KEY, "post_categoria" varchar(50) NOT NULL, "post_titulo" varchar(255) NOT NULL, "contenido" varchar(255) NOT NULL, "post_fecha" date NULL, "id_usuario_id" varchar(6) NOT NULL REFERENCES "USUARIO" ("id_usuario") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Visita
--
CREATE TABLE "VISITA" ("id_visita" varchar(6) NOT NULL PRIMARY KEY, "visi_fecha" date NULL, "visi_Estado" varchar(40) NULL, "id_mascota_id" varchar(6) NOT NULL REFERENCES "MASCOTA" ("id_mascota") DEFERRABLE INITIALLY DEFERRED, "id_sede_id" varchar(6) NOT NULL REFERENCES "SEDE" ("id_sede") DEFERRABLE INITIALLY DEFERRED, "id_usuario_id" varchar(6) NOT NULL REFERENCES "USUARIO" ("id_usuario") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "BLOGPOST_id_usuario_id_dc05a3e9" ON "BLOGPOST" ("id_usuario_id");
CREATE INDEX "VISITA_id_mascota_id_c97f5567" ON "VISITA" ("id_mascota_id");
CREATE INDEX "VISITA_id_sede_id_86f663b6" ON "VISITA" ("id_sede_id");
CREATE INDEX "VISITA_id_usuario_id_ee9ddfb8" ON "VISITA" ("id_usuario_id");
COMMIT;

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (pkgs: with pkgs; [
      flask
      requests
      sqlalchemy
      transformers
      pytorch
    ]))
  ];
}

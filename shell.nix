let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-25.05";
  pkgs = import nixpkgs {
    config = { };
    overlays = [ ];
  };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    (pkgs.python3.withPackages (
      ps: with ps; [
        boto3
        click
        hvac
        psutil
        pytest
      ]
    ))
  ];
}

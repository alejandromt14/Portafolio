% Script para multiplicar dos matrices nxn
% Solicita al usuario el tamaño de las matrices
n = input('Ingrese el tamaño n de las matrices cuadradas: ');

% Genera matrices aleatorias de tamaño nxn
A = randi([1, 10], n, n);
B = randi([1, 10], n, n);

% Muestra las matrices generadas
disp('Matriz A:');
disp(A);
disp('Matriz B:');
disp(B);

% Realiza la multiplicación
C = A * B;

% Muestra el resultado
disp('Resultado de la multiplicación A * B:');
disp(C);
%
% Suggested model answers to worksheet 2
%
% Ian Hawke, 14/14/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; LU decomposition
%
% This should really be written as a function, but here we just write the
% general algorithm for the matrix B.

disp('Question 1')

% Enter B first, and check the decomposition.
B = [64 8 48; 24 28 53; 32 49 91];
disp('Matlab LU decomposition gives')
[L,U]=lu(B)
disp('Checking this we have LU - B = ')
L*U - B
% Note that the LU decomposition algorithm now returns the permuted matrix,
% which is somewhat confusing. Instead we can use
% [L,U,P]=lu(B)
% which returns L, U as appropriate triangular matrices and P a permutation
% matrix, so that L * U = P * B.

% The LU decomposition algorithm using the Doolittle factorisation.

% Check the input is reasonable
if (not(isnumeric(B)))
    error('The input must be a numerical array!');
elseif (ndims(B)~=2)
    error('The input must be a 2-d array!');
elseif (size(B,1)~=size(B,2))
    error('The input must be a square 2-d array!');
end

% Set up L, U
L = zeros(size(B));
U = zeros(size(B));
for k = 1:size(B,1)
    L(k,k) = 1;
    U(k,k) = (B(k,k) - sum(L(k,1:k-1)*U(1:k-1,k))) / L(k,k);
    for j = k+1:size(B,1)
       U(k,j) = (B(k,j) - sum(L(k,1:k-1)*U(1:k-1,j))) / L(k,k);
    end
    for i = k+1:size(B,1)
       L(i,k) = (B(i,k) - sum(L(i,1:k-1)*U(1:k-1,k))) / U(k,k);
    end
end
disp('The Doolittle factorisation gives')
L
U
disp('Checking this we have LU - B = ')
L*U - B

% Coding question 2; Thomas algorithm.
% This is additional, so may not follow the notes closely.
% We will reduce matrix B to be tridiagonal - call it D

disp('Question 2')

% The matrix and RHS vector for D x = b
D = [64 8 0; 24 28 53; 0 49 91];
b = [3;2;1];

aa = diag(D,-1);
bb = diag(D, 0);
cc = diag(D, 1);
dd = b;
x = zeros(size(b));
for k = 2:size(D,1)
    m = aa(k-1) / bb(k-1);
    bb(k) = bb(k) - m*cc(k-1);
    dd(k) = dd(k) - m*dd(k-1);
end
x(end) = dd(end)./bb(end);
for k = size(D,1)-1:-1:1
    x(k) = (dd(k) - cc(k)*x(k+1)) ./ bb(k); 
end

disp('The answer that the Thomas algorithm gives is')
x
disp('The error compared to the Matlab answer is')
x - D\b

% Coding question 3; the Jacobi method
%
% This time we do implement it as a function to simplify applying it to two
% different matrices.

disp('Question 3')

% Enter the RHS vector
b = [3;2;1];

% Find the correct solution using Matlab methods.
x_exact = B\b;

% Take 30 steps using Jacobi
Nsteps = 30;
x = Worksheet2_MyJacobi(B, b, Nsteps);
% Compute the error from the exact solution
errs = zeros(size(x));
normerrs = zeros(Nsteps+1);
for i = 1:Nsteps+1
    errs(:,i) = x(:,i) - x_exact;
    normerrs(i) = norm(errs(:,i));
end
% Plots the error as a point in 3-space, and the norm of the vector error.
subplot(1,2,1)
plot3(errs(1,:),errs(2,:),errs(3,:),'bx')
xlabel('x');ylabel('y');zlabel('z');
subplot(1,2,2)
semilogy(normerrs)
xlabel('Nsteps');ylabel('|Error|')
title('Jacobi diverges for matrix B')

% Try the C matrix
C = [119/108 -14/27 -8/9; 7/54 46/27 7/9; 5/108 1/27 23/18];
% Find the correct solution using Matlab methods.
x_exact = C\b;

x = Worksheet2_MyJacobi(C, b, Nsteps);
% Compute the error from the exact solution
errs = zeros(size(x));
normerrs = zeros(Nsteps+1);
for i = 1:Nsteps+1
    errs(:,i) = x(:,i) - x_exact;
    normerrs(i) = norm(errs(:,i));
end
figure
subplot(1,2,1)
plot3(errs(1,:),errs(2,:),errs(3,:),'bx')
xlabel('x');ylabel('y');zlabel('z');
subplot(1,2,2)
semilogy(normerrs)
xlabel('Nsteps');ylabel('|Error|')
title('Jacobi converges for matrix C')

% Coding question 4; Gauss-Seidel

disp('Question 4')

x = Worksheet2_MyGaussSeidel(C, b, Nsteps);
% Compute the error from the exact solution
errs2 = zeros(size(x));
normerrs2 = zeros(Nsteps+1);
ind = zeros(Nsteps+1);
for i = 1:Nsteps+1
    errs2(:,i) = x(:,i) - x_exact;
    normerrs2(i) = norm(errs2(:,i));
    ind(i) = i-1;
end
figure
subplot(1,2,1)
plot3(errs2(1,:),errs2(2,:),errs2(3,:),'bx')
xlabel('x');ylabel('y');zlabel('z');
subplot(1,2,2)
semilogy(normerrs2)
xlabel('Nsteps');ylabel('|Error|')
title('Gauss-Seidel converges for matrix C')
% Compare Jacobi and Gauss-Seidel
figure
semilogy(ind,normerrs,'b-',ind,normerrs2,'k-');
xlabel('Nsteps');ylabel('|Error|')
legend('Jacobi','Gauss Seidel')

% Coding question 5; chord method

disp('Question 5')

% Set up the function
f = @(x)(tan(x) - exp(-x));

% We need 0 < m f' < 2 over the entire range; f' is between 2 and 4, so
% pick m = 1/2.

% Set up the contraction mapping for the chord method, m = 1/2.
g = @(x)(x - 0.5 * f(x));

%Pick x = 0 as the arbitrary starting point.
Nsteps = 10;
x = zeros(Nsteps+1,1);
ind = zeros(size(x));
for i = 1:Nsteps
    ind(i+1) = i;
    x(i+1) = g(x(i));
end
disp(sprintf('The estimated root after %i steps is %g, with function value %g', Nsteps, x(Nsteps+1), f(x(Nsteps+1))));
figure
semilogy(ind,abs(x-x(Nsteps+1)))
xlabel('Nsteps')



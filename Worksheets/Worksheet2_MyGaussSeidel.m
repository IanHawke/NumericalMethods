%
% function x = Worksheet2_MyGaussSeidel(A, b, Nsteps)
%
% Applies the Gauss-Seidel method to try and find the solution of the linear
% system A x = b, taking Nsteps steps and starting from the trivial guess. 
%
% Expects a square 2-D matrix A. 
%
function x = Worksheet2_MyGaussSeidel(A, b, Nsteps)

% Check the input is reasonable
if (not(isnumeric(A)))
    error('The input must be a numerical array!');
elseif (ndims(A)~=2)
    error('The input must be a 2-d array!');
elseif (size(A,1)~=size(A,2))
    error('The input must be a square 2-d array!');
end

% Set up the output
x = zeros(length(b), Nsteps+1);

% Set up the normalized A matrix and b vector
Anorm = A;
bnorm = b;
for i=1:size(A,1)
    bnorm(i) = b(i) / A(i,i);
    Anorm(i,:) = A(i,:) / A(i,i);
end

% Compute the split; first Jacobi N and P
JN = eye(size(Anorm));
JP = JN - Anorm;
% Split the Jacobi P into lower and upper triangular parts
AL = tril(JP);
AU = triu(JP);
% Compute N and P for Gauss-Seidel
N = eye(size(Anorm)) - AL;
P = AU;

% Check whether we expect this matrix to converge or not.
M = inv(N)*P;
d = eigs(M);
if (abs(d(1)) > 1)
    disp(sprintf('The largest eigenvalue of the convergence matrix is %g, so Gauss-Seidel will not converge',abs(d(1))))
else
    disp(sprintf('The largest eigenvalue of the convergence matrix is %g, so Gauss-Seidel should converge',abs(d(1))))
end

% Apply the iteration scheme
for j = 1:Nsteps
    for i = 1:length(b)
        x(i,j+1) = bnorm(i) + sum(AL(i,1:i-1) * x(1:i-1,j+1)) + AU(i,:) * x(:,j);
    end
end
    
end

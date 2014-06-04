%
% function x = Worksheet2_MyJacobi(A, b, Nsteps)
%
% Applies the Jacobi method to try and find the solution of the linear
% system A x = b, taking Nsteps steps and starting from the trivial guess. 
%
% Expects a square 2-D matrix A. 
%
function x = Worksheet2_MyJacobi(A, b, Nsteps)

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

% Compute the split; first N and P
N = eye(size(Anorm));
P = N - Anorm;
% Split P into lower and upper triangular parts
AL = tril(P);
AU = triu(P);

% Check whether we expect this matrix to converge or not.
M = inv(N)*P;
d = eigs(M);
if (abs(d(1)) > 1)
    disp(sprintf('The largest eigenvalue of the convergence matrix is %g, so Jacobi will not converge',abs(d(1))))
else
    disp(sprintf('The largest eigenvalue of the convergence matrix is %g, so Jacobi should converge',abs(d(1))))
end

% Apply the iteration scheme
for j = 1:Nsteps
    x(:,j+1) = bnorm + (AL + AU) * x(:,j);
end
    
end

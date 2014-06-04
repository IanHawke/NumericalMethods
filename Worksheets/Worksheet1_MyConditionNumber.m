%
% function ConditionNumber = Worksheet1_MyConditionNumber(A)
%
% Computes the condition number of the input matrix A.
%
% Expects a square 2-D matrix A. It will complain if the condition number
% is larger than 10 (this is a ludicrously low bound, but tests that the
% function actually works with the default input).
%
function ConditionNumber = Worksheet1_MyConditionNumber(A)

% Check the input is reasonable
if (not(isnumeric(A)))
    error('The input must be a numerical array!');
elseif (ndims(A)~=2)
    error('The input must be a 2-d array!');
elseif (size(A,1)~=size(A,2))
    error('The input must be a square 2-d array!');
end

% Set up the maximum condition number
Max_ConditionNumber = 10;

% Compute the condition number
ConditionNumber = cond(A);

if (ConditionNumber > Max_ConditionNumber)
    disp(sprintf('The condition number, %g, of the matrix makes it not suitably well-conditioned (bigger than %g)', ...
        ConditionNumber, Max_ConditionNumber));
end

end
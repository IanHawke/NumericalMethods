%
% Suggested model answers to worksheet 1
%
% Ian Hawke, 14/14/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; matrices

disp('Question 1')

A1 = [1 2; 3 4]
A2 = [-3 2; 3 6]

disp('The transpose of the matrices are')
A1.'
A2.'

disp('The inverse of the matrices are')
inv(A1)
inv(A2)

% Coding question 2; norms and condition numbers

disp('Question 2')

v1 = [1;3;-1];
v2 = [1;-2];
v3 = [1;6;-3;1];

disp('The vector 1-norms are')
norm(v1,1)
norm(v2,1)
norm(v3,1)
disp('The vector 2-norms are')
norm(v1,2)
norm(v2,2)
norm(v3,2)
disp('The vector infinity-norms are')
norm(v1,inf)
norm(v2,inf)
norm(v3,inf)

disp('The matrix 1-norms are')
norm(A1,1)
norm(A2,1)
disp('The matrix infinity-norms are')
norm(A1,inf)
norm(A2,inf)

% Coding question 3; writing a function

disp('Question 3')

Worksheet1_MyConditionNumber(A1)
Worksheet1_MyConditionNumber(A2)

% Coding question 4; bisection method

disp('Question 4')

% Set up the tolerance in the width of the interval
tolerance = 1e-15;
% Set up the initial bracketing interval
x_lo = 0;
x_hi = 1;

% Set up the function and the initial function values.
f = @(x)(tan(x) - exp(-x));
f_lo = f(x_lo);
f_hi = f(x_hi);

% Check that we really bracket a root properly
if (f_lo * f_hi > 0)
    error('The initial interval does not properly bracket a root!')
end

% Set up the bisection loop.
x_guess = (x_lo + x_hi) / 2;
f_guess = f(x_guess);

% Loop until the root is bracketed within the tolerance.
while (x_hi - x_lo > tolerance)
   
    if (f_lo * f_guess < 0)
       % The root is between the guessed value and the lower bound
       x_hi = x_guess;
       f_hi = f_guess;
    else
       % The root is between the guessed value and the upper bound
       x_lo = x_guess;
       f_lo = f_guess;
    end
    
    % Set the new bisection estimate
    x_guess = (x_lo + x_hi) / 2;
    f_guess = f(x_guess);
    
end

disp(sprintf('The final value of x is \n  %18.12g \nwhere the value of f is \n %18.12g', ...
    x_guess, f_guess));

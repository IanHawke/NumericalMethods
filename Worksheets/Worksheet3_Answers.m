%
% Suggested model answers to worksheet 3
%
% Ian Hawke, 14/14/08
%

% Clear all starting values.
clear;
close all;
clc;

% Coding question 1; quadrature

disp('Question 1')

% Set up the different functions to be computed
f1 = @(x)(sin(pi.*x).^2);
f2 = @(x)(exp(-x).*sinh(x));
f3 = @(x)(1./sqrt(x));

% Test Simpson's rule
options.quadrature = 'Simpson';
ans1 = Worksheet3_MyQuadrature(f1, [0 1], options);
disp(sprintf('Simpson''s rule, first integral gives %g (error %g)', ans1, 0.5-ans1));
ans2 = Worksheet3_MyQuadrature(f2, [0 1], options);
disp(sprintf('Simpson''s rule, second integral gives %g (error %g)', ans2, 0.283833821-ans2));
ans3 = Worksheet3_MyQuadrature(f3, [0 1], options);
disp(sprintf('Simpson''s rule, third integral gives %g (error %g)', ans3, 2-ans3));

% Test trapezoidal rule
options.quadrature = 'Trapezoidal';
ans1 = Worksheet3_MyQuadrature(f1, [0 1], options);
disp(sprintf('Trapezoidal rule, first integral gives %g (error %g)', ans1, 0.5-ans1));
ans2 = Worksheet3_MyQuadrature(f2, [0 1], options);
disp(sprintf('Trapezoidal rule, second integral gives %g (error %g)', ans2, 0.283833821-ans2));
ans3 = Worksheet3_MyQuadrature(f3, [0 1], options);
disp(sprintf('Trapezoidal rule, third integral gives %g (error %g)', ans3, 2-ans3));

disp('We note that both the above rules fail for the final test, as the integrand is singular at x=0!');

% Test Gauss quadrature
options.quadrature = 'Gauss';
ans1 = Worksheet3_MyQuadrature(f1, [0 1], options);
disp(sprintf('Gauss quadrature, first integral gives %g (error %g)', ans1, 0.5-ans1));
ans2 = Worksheet3_MyQuadrature(f2, [0 1], options);
disp(sprintf('Gauss quadrature, second integral gives %g (error %g)', ans2, 0.283833821-ans2));
ans3 = Worksheet3_MyQuadrature(f3, [0 1], options);
disp(sprintf('Gauss quadrature, third integral gives %g (error %g)', ans3, 2-ans3));

% Coding question 2; secant method

disp('Question 2')

f = @(x)(tan(x) - exp(-x));

% This method cannot be put in contraction mapping form, so we work
% directly with the function f above.

% We need two initial guesses; we put down the boundaries of the interval.
Nsteps = 10;
x = zeros(Nsteps+2);
x(2) = 1;
ind = zeros(size(x));
ind(2) = 1;
for i = 1:Nsteps
    ind(i+2) = i;
    x(i+2) = x(i+1) - f(x(i+1)) * (x(i+1) - x(i)) ./ (f(x(i+1)) - f(x(i)));
end
disp(sprintf('The estimated root after %i steps is %g, with function value %g', Nsteps, x(Nsteps+1), f(x(Nsteps+1))));
semilogy(ind,abs(x-x(Nsteps+1)))
xlabel('Nsteps')

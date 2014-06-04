%
% function t = Worksheet4_MyRK4(f, y0, interval, Nsteps)
%
% Solve the ODE y' = f(x, y) on the given interval taking Nsteps with
% initial data y0.
%
function yend = Worksheet4_MyRK4(f, y0, interval, Nsteps)

% Check the input is reasonable
if (not(isa(f, 'function_handle')))
    error('First argument must be a function handle!')
elseif ((not(isnumeric(interval)))&&(ndims(interval)~=1)&&(length(interval)~=2))
    error('Second argument must define the interval; a 1d length 2 numeric array!')
end

h = (interval(2) - interval(1)) / Nsteps;
x = linspace(interval(1), interval(2), Nsteps+1);
y = zeros(size(x));
y(1) = y0;

for i = 1:Nsteps
    k1 = h * f(x(i), y(i));
    k2 = h * f(x(i) + h/2, y(i) + k1/2);
    k3 = h * f(x(i) + h/2, y(i) + k2/2);
    k4 = h * f(x(i) + h  , y(i) + k3  );
    y(i+1) = y(i) + (k1 + k4 + 2*(k2 + k3))/6;
end

yend = y(end);

end

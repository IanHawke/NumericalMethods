%
% function x = Worksheet3_MyQuadrature(f, interval, options)
%
% Approximate the integral of a function f over the given interval using
% various methods.
%
function I = Worksheet3_MyQuadrature(f, interval, options)

% Check the input is reasonable
if (not(isa(f, 'function_handle')))
    error('First argument must be a function handle!')
elseif ((not(isnumeric(interval)))&&(ndims(interval)~=1)&&(length(interval)~=2))
    error('Second argument must define the interval; a 1d length 2 numeric array!')
elseif (not(isstruct(options)))
    error('Third argument must be an options structure!')
elseif (not(isfield(options,'quadrature')))
    error('quadrature field must be set in the options!')
end

I = 0;

switch options.quadrature
    case 'Simpson'
        % We use 3 points.
        N = 3;
        % Compute h
        h = (interval(2) - interval(1)) / (N-1);
        % Shorthands for point locations
        x0 = interval(1);
        x2 = interval(2);
        x1 = (x0 + x2) / 2;
        % Simpson's rule
        I = h/3 * (f(x0) + f(x2) + 4*f(x1));
    case 'Trapezoidal'
        % We use 3 points.
        N = 3;
        % Compute h
        h = (interval(2) - interval(1)) / (N-1);
        % Shorthands for point locations
        x0 = interval(1);
        x2 = interval(2);
        x1 = (x0 + x2) / 2;
        % Trapezoidal rule
        I = h/2 * (f(x0) + f(x2) + 2*f(x1));
    case 'Gauss'
        % We use three nodes and weights
        % First give them on the interval [-1,1] (you should check these!)
        x(1) = -sqrt(3/5);
        w(1) = 5/9;
        x(2) = 0;
        w(2) = 8/9;
        x(3) = sqrt(3/5);
        w(3) = 5/9;
        % Remap [-1,1] to given interval
        x = (x + 1) * (interval(2) - interval(1)) / 2 + interval(1);
        I = w(1) * f(x(1)) + w(2) * f(x(2)) + w(3) * f(x(3));
        % Reweight integral
        I = (interval(2) - interval(1)) / 2 * I;
    otherwise
        error('The quadrature option is not recognized!')
end
    
end

package Moose::Exception::CouldNotGenerateInlineAttributeMethod;
our $VERSION = '2.1807';

use Moose;
extends 'Moose::Exception';
with 'Moose::Exception::Role::Instance';

has 'option' => (
    is       => 'ro',
    isa      => 'Str',
    required => 1
);

has 'error' => (
    is       => 'ro',
    isa      => 'Str|Moose::Exception',
    required => 1
);

sub _build_message {
    my $self = shift;
    "Could not generate inline ".$self->option." because : ".$self->error;
}

1;
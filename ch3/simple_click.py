#!/usr/bin/python3

import click

@click.command()
@click.option('--mqtype', default='Mqtt', help='type of mq system')
@click.option('--broker', default='Azure', help='Broker provider')
def call(mqtype, broker):
    print(f"using {mqtype} as message queue, connecting to {broker}...")
    
if __name__== '__main__':
    call()

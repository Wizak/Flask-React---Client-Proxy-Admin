import React from 'react';
import {List, Datagrid, TextField} from 'react-admin';

export const UserList = props => (
    <List {...props}>
        <Datagrid>
            <TextField source="id" />
            <TextField source="src" />
        </Datagrid>
    </List>
);
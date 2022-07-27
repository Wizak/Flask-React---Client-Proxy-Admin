import React from 'react';
import {List, Datagrid, TextField} from 'react-admin';

export const VisitorList = props => (
    <List {...props}>
        <Datagrid>
            <TextField source="id" />
            <TextField source="end_user_id" />
            <TextField source="web_page_url" />
            <TextField source="date" />
        </Datagrid>
    </List>
);
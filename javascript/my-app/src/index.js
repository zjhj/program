import React from 'react';
import ReactDOM from 'react-dom';
import TodoList from './TodoList';

ReactDOM.render(<TodoList />, document.getElementById('root'));
// import React, { useState } from 'react';
// import ReactDOM from 'react-dom';
// import 'antd/dist/antd.css';
// import { EyeInvisibleOutlined, EyeTwoTone } from '@ant-design/icons';
// import {
//   Form,
//   Input,
//   Button,
//   Radio,
//   Select,
//   DatePicker,
//   Space
// } from 'antd';
// const tailLayout = {
//   wrapperCol: { offset: 8, span: 8 },
// };
// const FormSizeDemo = () => {
//   const [componentSize, setComponentSize] = useState('default');
//   const onFormLayoutChange = ({ size }) => {
//     setComponentSize(size);
//   };
//   return (
//     <>
//       <Form
//         labelCol={{ span: 8 }}
//         wrapperCol={{ span: 8 }}
//         layout="horizontal"
//         initialValues={{ size: componentSize }}
//         onValuesChange={onFormLayoutChange}
//         size={componentSize}
//       >
//         <Form.Item label="用户名">
//           <Input />
//         </Form.Item>
//         <Form.Item label="密码">
//
//             <Input.Password
//               placeholder="input password"
//               iconRender={visible => (visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />)}
//             />
//
//         </Form.Item>
//         <Form.Item label="性别" name="size">
//           <Radio.Group>
//             <Radio value="0">男</Radio>
//             <Radio value="1">女</Radio>
//           </Radio.Group>
//         </Form.Item>
//         <Form.Item label="学历">
//           <Select>
//             <Select.Option value="0">大学</Select.Option>
//             <Select.Option value="1">高中</Select.Option>
//           </Select>
//         </Form.Item>
//
//         <Form.Item label="生日">
//           <DatePicker />
//         </Form.Item>
//         <Form.Item {...tailLayout}>
//           <Button type={"primary"} htmlType="submit">提交</Button>
//         </Form.Item>
//       </Form>
//     </>
//   );
// };
// ReactDOM.render(<FormSizeDemo />, document.getElementById('root'));

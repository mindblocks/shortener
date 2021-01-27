
import React from "react";
import axios from "axios";
import { Component } from "react";
import Clipboard from "react-clipboard.js";
import { Button, notification } from 'antd';
import env from "./env.js";
import 'antd/dist/antd.css';
import {HiCheckCircle} from"react-icons/hi"
import {VscError} from"react-icons/vsc"
import {AiOutlineCopy} from"react-icons/ai"
const mainFonts = require("./styles/fonts.css");
const mainStyles = require("./styles/main.css");

const Sueccess = {
  message: 'Done !',
  description:
  'URL Created Successfully',
  icon: <HiCheckCircle color="green"/>
};

const Fallied= {
  message: 'Error ',
  description:
  'Its Either Bad URL or Request Error',
  icon:<VscError color="red"/>
};

export default class ShortenerApp extends Component {
  constructor() {
    super();
    this.state = {
      showInput: false,
      ShowResult: false,
      Slug:"",
      errMsg: "",
      data: { slug: "", url: "" },
    };
  }

  showInput = (ture) => {
    this.setState(ture);
  };

  handleChange = (e, key) => {
    let data = this.state.data;
    data[key] = e.target.value;
    this.setState({ data });
  };

  handleSubmit = () => {
    axios.post(env.API,this.state.data)
      .then((response) => {
        notification.open(Sueccess);
        this.setState({ ShowResult: true ,Slug:response.data.slug});

      })
      .catch((error) =>
        notification.open(Fallied));

  };

  render() {
    const slug = this.state.Slug;
    const shortUrl = env.HOST + slug;
    const args = {
      message: 'Coped !',

      icon:<AiOutlineCopy color="black"/>
    };
    return (
      <div className="limiter">
      <div className="container-login100">
      <div className="wrap-login100 p-b-160 p-t-50">
      {this.state.ShowResult ? (
        <div className="login100-form validate-form">
        <div className="descriptionContainer">
        <p className="description">Your URL is created successfully</p>
        </div>
        <div
        className="showShortUrl rs1 validate-input"
        data-validate="URL is required"
        >


        <a className="url"href={shortUrl} target="_blank">{shortUrl}</a>
        </div>

        <div className="container-login100-form-btn">

        <Clipboard className="login100-form-btn"
        onSuccess={

          () => notification.open(args)
        }

        data-clipboard-text={shortUrl}>
        <span className="btn-color">Copy</span>
        </Clipboard>
        </div>
        </div>
      ) : (
        <div className="login100-form validate-form">
        <div className="descriptionContainer">
        <p className="description">Make URLs Shorter, enter your URL and enter custom slug if you like or leave it empty</p>
        </div>

        <div
        className="wrap-input100 rs1 validate-input"
        data-validate="Username is required"
        >
        <input
        className="input100"
        type="text"
        name="username"
        onChange={(e) => this.handleChange(e, "url")}
        />
        <span className="label-input100">URL Link</span>
        </div>

        <div
        className="wrap-input100 rs2 validate-input"
        data-validate="Password is required"
        >
        <input
        className="input100"
        type="text"
        name="pass"
        onChange={(e) => this.handleChange(e, "slug")}
        />
        <span className="label-input100">Slug</span>
        </div>

        <div className="container-login100-form-btn">
        <button
        className="login100-form-btn"
        onClick={this.handleSubmit}
        >
        Create
        </button>
        </div>
        </div>
      )}
      </div>
      </div>
      </div>
  );
  }
}

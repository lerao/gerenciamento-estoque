/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50736
 Source Host           : localhost:3306
 Source Schema         : estoque

 Target Server Type    : MySQL
 Target Server Version : 50736
 File Encoding         : 65001

 Date: 19/10/2023 21:37:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for categorias
-- ----------------------------
DROP TABLE IF EXISTS `categorias`;
CREATE TABLE `categorias`  (
  `id` int(11) NOT NULL,
  `nome` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for fornece
-- ----------------------------
DROP TABLE IF EXISTS `fornece`;
CREATE TABLE `fornece`  (
  `cnpj_loja` bigint(14) NOT NULL,
  `cnpj_fornecedor` bigint(14) NOT NULL,
  `id_produto` int(11) NOT NULL,
  `data` datetime(0) NULL DEFAULT NULL,
  `qtd` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `preco_total` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cnpj_loja`, `cnpj_fornecedor`, `id_produto`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for fornecedores
-- ----------------------------
DROP TABLE IF EXISTS `fornecedores`;
CREATE TABLE `fornecedores`  (
  `cnpj` bigint(14) NOT NULL,
  `razaosocial` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `nomefantasia` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `logradouro` varchar(80) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `uf` varchar(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cidade` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `telefone` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cnpj`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for lojas
-- ----------------------------
DROP TABLE IF EXISTS `lojas`;
CREATE TABLE `lojas`  (
  `cnpj` bigint(14) NOT NULL,
  `razaosocial` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `nomefantasia` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `logradouro` varchar(80) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `uf` varchar(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `cidade` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `telefone` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `instagram` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `facebook` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `twitter` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cnpj`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for produtos
-- ----------------------------
DROP TABLE IF EXISTS `produtos`;
CREATE TABLE `produtos`  (
  `cod` int(11) NOT NULL,
  `nome` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `id_categoria` int(11) NULL DEFAULT NULL,
  `marca` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `qtd` int(11) NULL DEFAULT NULL,
  `und_medida` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `observacao` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`cod`) USING BTREE,
  INDEX `fkCategoria`(`id_categoria`) USING BTREE,
  CONSTRAINT `fkCategoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for produtos_precos
-- ----------------------------
DROP TABLE IF EXISTS `produtos_precos`;
CREATE TABLE `produtos_precos`  (
  `id` int(11) NOT NULL,
  `id_produto` int(11) NULL DEFAULT NULL,
  `preco_compra` double(16, 2) NULL DEFAULT NULL,
  `preco_venda` double(16, 2) NULL DEFAULT NULL,
  `data_inicio` datetime(0) NULL DEFAULT NULL,
  `data_fim` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
